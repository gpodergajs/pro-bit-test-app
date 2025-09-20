import { Injectable, inject } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, Observable, tap, throwError } from 'rxjs';
import { UserType } from '../../../core/enum/user-type.enum';

export interface LoginResponse {
  access_token: string; // JWT token returned by backend
}

@Injectable({
  providedIn: 'root',
})
export class AuthService {
private http = inject(HttpClient);

private readonly apiUrl = '/api/auth';
  private readonly tokenKey = 'auth_token';
  private useLocalStorage = false;

  /**
   * Logs in the user
   * @param username
   * @param password
   * @param rememberMe - if true, token is stored in localStorage
   */
  login(username: string, password: string, rememberMe = false): Observable<LoginResponse> {
    this.useLocalStorage = rememberMe; // set storage preference dynamically
    const url = `${this.apiUrl}/login`;

    return this.http.post<LoginResponse>(url, { username, password }).pipe(
      tap((res) => this.setToken(res.access_token)),
      catchError((error) => {
        console.error('Login failed:', error);
        return throwError(() => error);
      })
    );
  }

  /**
   * Save JWT token
   */
  private setToken(token: string) {
    if (this.useLocalStorage) {
      localStorage.setItem(this.tokenKey, token);
    } else {
      sessionStorage.setItem(this.tokenKey, token);
    }
  }

  /**
   * Get JWT token
   */
  getToken(): string | null {
    return localStorage.getItem(this.tokenKey) || sessionStorage.getItem(this.tokenKey);
  }

  /**
   * Check if user is logged in
   */
  isLoggedIn(): boolean {
    const token = this.getToken();
    if (!token) return false;

    const payloadBase64 = token.split('.')[1];
    if (!payloadBase64) return false;

    try {
      const payload = JSON.parse(atob(payloadBase64));
      if (payload.exp && Date.now() >= payload.exp * 1000) return false;
      return true;
    } catch (e) {
      console.error('Invalid token', e);
      return false;
    }
  }

  /**
   * Logs out the user
   */
  logout() {
    localStorage.removeItem(this.tokenKey);
    sessionStorage.removeItem(this.tokenKey);
  }

  /**
   * Helper to create Authorization header
   */
  getAuthHeaders(): HttpHeaders {
    const token = this.getToken();
    return new HttpHeaders({
      Authorization: token ? `Bearer ${token}` : '',
    });
  }

    /** Return decoded payload or null on error */
  getTokenPayload(): TokenPayload | null {
    const token = this.getToken();
    if (!token) return null;
    const parts = token.split('.');
    if (parts.length < 2) return null;
    const payloadBase64 = parts[1];
    try {
      // atob can throw if malformed
      const json = atob(payloadBase64);
      return JSON.parse(json);
    } catch (e) {
      console.error('Failed to decode token payload', e);
      return null;
    }
  }

  /** Return numeric user_type_id or null */
  getUserTypeId(): number | null {
    const payload = this.getTokenPayload();
    if (!payload) return null;
    const raw = payload.user_type_id ?? payload.user_type ?? null;
    if (raw == null) return null;
    const num = Number(raw);
    return Number.isNaN(num) ? null : num;
  }

  /** Convenience check */
  isAdmin(): boolean {
    const id = this.getUserTypeId();

    return id === UserType.Admin;
  }


}
