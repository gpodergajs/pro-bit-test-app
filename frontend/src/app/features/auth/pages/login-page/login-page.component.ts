import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { FormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { CommonModule } from '@angular/common';
import { MatCardModule } from '@angular/material/card';
import { ProgressBarComponent } from '../../../../shared/components/progress-bar/progress-bar.component';
import { MatCheckboxModule } from '@angular/material/checkbox'; 


@Component({
  selector: 'app-login-page',
  imports: [CommonModule, FormsModule, MatFormFieldModule, MatInputModule, MatButtonModule, MatCardModule, ProgressBarComponent, MatCheckboxModule  ],
  templateUrl: './login-page.component.html',
  styleUrl: './login-page.component.scss',
  standalone: true
})
export class LoginPageComponent {
  username: string = '';
  password: string = '';
  loading: boolean = false;
  rememberMe: boolean = false;

  constructor(private authService: AuthService, private router: Router) {}

  onSubmit() {
     if (!this.username || !this.password) return;

  this.loading = true;

  this.authService.login(this.username, this.password, this.rememberMe).subscribe({
    next: () => {
      this.loading = false;
      alert('Login successful!');
      this.router.navigate(['/cars']);
    },
    error: (err) => {
      this.loading = false;
      alert('Login failed: ' + (err.error?.message || err.message));
    },
  });
}
}
