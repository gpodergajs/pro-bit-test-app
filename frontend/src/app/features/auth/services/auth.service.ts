import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, Observable, tap, throwError } from 'rxjs';

export interface LoginResponse {
  access_token: string; // JWT token returned by backend
}

@Injectable({
  providedIn: 'root',
})
export class AuthService {
    private readonly apiUrl = '/api/auth'; // Remove http://localhost:5000
  private tokenKey = 'auth_token';

  constructor(private http: HttpClient) {}

  /**
   * Logs in the user
   * @param username
   * @param password
   * @returns Observable<LoginResponse>
   */
  login(username: string, password: string): Observable<LoginResponse> {
    const url = `${this.apiUrl}/login`;
    return this.http.post<LoginResponse>(url, { username, password }).pipe(
      tap((res) => this.setToken(res.access_token)),
      catchError((error) => {
        // optionally log it
        console.error('Login failed:', error);
        return throwError(() => error);
      })
    );
  }

  /**
   * Save JWT token to localStorage
   * @param token
   */
  private setToken(token: string) {
    localStorage.setItem(this.tokenKey, token);
  }

  /**
   * Get JWT token from localStorage
   */
  getToken(): string | null {
    return localStorage.getItem(this.tokenKey);
  }

  /**
   * Check if user is logged in
   */
  isLoggedIn(): boolean {
    console.log('Checking login status...');
    const token = this.getToken();
    if (!token) return false;

    const payloadBase64 = token.split('.')[1];
    if (!payloadBase64) return false;

    try {
      const payload = JSON.parse(atob(payloadBase64));
      // Optional: check token expiration
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


}
