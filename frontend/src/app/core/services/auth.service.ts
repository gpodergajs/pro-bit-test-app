import { Injectable, inject } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Observable, tap, throwError } from 'rxjs'; // Removed catchError
import { UserType } from '../enum/user-type.enum';
import { ErrorHandlingService } from './error-handling.service';

// Removed LoginResponse interface

export interface TokenPayload {
  exp: number;
  user_type_id?: number;
  user_type?: number;
}

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private http = inject(HttpClient);
  private errorHandlingService = inject(ErrorHandlingService);

  private readonly tokenKey = 'auth_token';
  private useLocalStorage = false; // This will be managed by setUseLocalStorage

  // New method to set storage preference
  setUseLocalStorage(rememberMe: boolean) {
    this.useLocalStorage = rememberMe;
  }

  // Made public for LoginService
  setToken(token: string) {
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
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } catch (error: any) {
      this.errorHandlingService.showError(this.errorHandlingService.getErrorMessage(error));
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
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } catch (error: any) {
      this.errorHandlingService.showError(this.errorHandlingService.getErrorMessage(error));
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