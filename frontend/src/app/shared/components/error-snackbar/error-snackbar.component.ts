import { Component, Input, inject } from '@angular/core';
import { MatSnackBarModule, MatSnackBarRef } from '@angular/material/snack-bar';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-error-snackbar',
  standalone: true,
  imports: [MatSnackBarModule, MatButtonModule],
  templateUrl: './error-snackbar.component.html',
  styleUrl: './error-snackbar.component.scss',
})
export class ErrorSnackbarComponent {
  @Input() message = 'An unexpected error occurred.';

  snackBarRef = inject(MatSnackBarRef);

  dismiss() {
    this.snackBarRef.dismiss();
  }
}
