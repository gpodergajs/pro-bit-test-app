import { Injectable, inject } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { HttpErrorResponse } from '@angular/common/http';
import { SnackbarComponent } from '../../shared/components/snackbar/snackbar.component'; // Updated import
import { ErrorHandlingService } from './error-handling.service'; // Import the original ErrorHandlingService

@Injectable({
  providedIn: 'root',
})
export class MessageService {
  private snackBar = inject(MatSnackBar);
  private errorHandlingService = inject(ErrorHandlingService); // Inject the original ErrorHandlingService

  showSuccess(message: string, duration: number = 3000) {
    this.snackBar.openFromComponent(SnackbarComponent, {
      data: { message: message, type: 'success' }, // Pass type
      duration: duration,
      panelClass: ['success-snackbar'], // Use the success-snackbar class
    });
  }

  showError(error: HttpErrorResponse | Error | string, duration: number = 5000) {
    const errorMessage = this.errorHandlingService.getErrorMessage(error as HttpErrorResponse); // Leverage ErrorHandlingService
    this.snackBar.openFromComponent(SnackbarComponent, {
      data: { message: errorMessage, type: 'error' }, // Pass type
      duration: duration,
      panelClass: ['error-snackbar'], // Use the error-snackbar class
    });
  }
}
