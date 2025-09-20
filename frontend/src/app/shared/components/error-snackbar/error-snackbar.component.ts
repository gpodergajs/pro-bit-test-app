import { Component, inject } from '@angular/core';
import { MatSnackBarModule, MatSnackBarRef, MAT_SNACK_BAR_DATA } from '@angular/material/snack-bar';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-error-snackbar',
  standalone: true,
  imports: [MatSnackBarModule, MatButtonModule],
  templateUrl: './error-snackbar.component.html',
  styleUrl: './error-snackbar.component.scss',
})
export class ErrorSnackbarComponent {
  message: string;

  snackBarRef = inject(MatSnackBarRef);
  private data = inject(MAT_SNACK_BAR_DATA);

  constructor() {
    this.message = this.data.message || 'An unexpected error occurred.';
  }

  dismiss() {
    this.snackBarRef.dismiss();
  }
}
