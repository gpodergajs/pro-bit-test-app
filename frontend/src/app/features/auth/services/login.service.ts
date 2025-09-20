import { Injectable, inject } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { catchError, Observable, tap, throwError } from 'rxjs';
import { MessageService } from '../../../../core/services/message.service'; // Import MessageService
import { AuthService } from '../../../../core/services/auth.service';

export interface LoginResponse {
  access_token: string; // JWT token returned by backend
}

@Injectable({
  providedIn: 'root',
})
export class LoginService {
  private http = inject(HttpClient);
  private messageService = inject(MessageService); // Inject MessageService
  private authService = inject(AuthService); // Inject AuthService to call setToken

  private readonly apiUrl = '/api/auth';

  /**
   * Logs in the user
   * @param username
   * @param password
   * @param rememberMe - if true, token is stored in localStorage
   */
  login(username: string, password: string, rememberMe = false): Observable<LoginResponse> {
    this.authService.setUseLocalStorage(rememberMe); // Set storage preference via AuthService
    const url = `${this.apiUrl}/login`;

    return this.http.post<LoginResponse>(url, { username, password }).pipe(
      tap((res) => this.authService.setToken(res.access_token)), // Use AuthService to set token
      catchError((error: HttpErrorResponse) => {
        this.messageService.showError(error); // Use MessageService
        return throwError(() => error);
      })
    );
  }
}
