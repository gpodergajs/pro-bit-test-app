import { Component, inject } from '@angular/core';
import { MatSnackBarModule, MatSnackBarRef, MAT_SNACK_BAR_DATA } from '@angular/material/snack-bar';
import { MatButtonModule } from '@angular/material/button';
import { CommonModule } from '@angular/common'; // Import CommonModule for ngClass

interface SnackbarData {
  message: string;
  type: 'success' | 'error';
}

@Component({
  selector: 'app-snackbar',
  standalone: true,
  imports: [MatSnackBarModule, MatButtonModule, CommonModule],
  templateUrl: './snackbar.component.html',
  styleUrl: './snackbar.component.scss',
})
export class SnackbarComponent {
  message: string;
  type: 'success' | 'error';

  snackBarRef = inject(MatSnackBarRef);
  private data: SnackbarData = inject(MAT_SNACK_BAR_DATA);

  constructor() {
    this.message = this.data.message || 'An unexpected error occurred.';
    this.type = this.data.type || 'error'; // Default to error if type is not provided
  }

  dismiss() {
    this.snackBarRef.dismiss();
  }
}
