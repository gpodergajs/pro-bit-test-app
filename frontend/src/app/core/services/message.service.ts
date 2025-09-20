import { Injectable, inject } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { HttpErrorResponse } from '@angular/common/http';
import { SnackbarComponent } from '../../shared/components/snackbar/snackbar.component';
import { ErrorHandlingService } from './error-handling.service';

@Injectable({
  providedIn: 'root',
})
export class MessageService {
  private snackBar = inject(MatSnackBar);
  private errorHandlingService = inject(ErrorHandlingService); 

  showSuccess(message: string, duration: number = 3000) {
    this.snackBar.openFromComponent(SnackbarComponent, {
      data: { message: message, type: 'success' },
      duration: duration,
      panelClass: ['success-snackbar'], 
    });
  }

  showError(error: HttpErrorResponse | Error | string, duration: number = 5000) {
    const errorMessage = this.errorHandlingService.getErrorMessage(error as HttpErrorResponse); 
    this.snackBar.openFromComponent(SnackbarComponent, {
      data: { message: errorMessage, type: 'error' },
      duration: duration,
      panelClass: ['error-snackbar'],
    });
  }
}
