import { Injectable, inject } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { ErrorSnackbarComponent } from '../../shared/components/error-snackbar/error-snackbar.component';
import { HttpErrorResponse } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class ErrorHandlingService {
  private snackBar = inject(MatSnackBar);

  showError(message: string) {
    this.snackBar.openFromComponent(ErrorSnackbarComponent, {
      data: { message: message },
      duration: 5000,
      panelClass: ['error-snackbar'],
    });
  }

  getErrorMessage(error: HttpErrorResponse | Error | string): string {
    console.log(error)
    if (error instanceof HttpErrorResponse) {
      if (error.error && error.error.message) {
        return error.error.message;
      } else if (error.message) {
        return error.message;
      } else {
        return 'An HTTP error occurred.';
      }
    } else if (error instanceof Error) {
      return error.message;
    } else if (typeof error === 'string') {
      return error;
    } else {
      return 'An unexpected error occurred.';
    }
  }
}
