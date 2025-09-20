import { Component, inject } from '@angular/core';
import { Router } from '@angular/router';
import { LoginService } from '../../services/login.service'; // Updated import
import { FormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { CommonModule } from '@angular/common';
import { MatCardModule } from '@angular/material/card';
import { ProgressBarComponent } from '../../../../shared/components/progress-bar/progress-bar.component';
import { MatCheckboxModule } from '@angular/material/checkbox'; 
import { MessageService } from '../../../../core/services/message.service';


@Component({
  selector: 'app-login-page',
  imports: [CommonModule, FormsModule, MatFormFieldModule, MatInputModule, MatButtonModule, MatCardModule, ProgressBarComponent, MatCheckboxModule  ],
  templateUrl: './login-page.component.html',
  styleUrl: './login-page.component.scss',
  standalone: true
})
export class LoginPageComponent {
  private loginService = inject(LoginService); // Updated injection
  private router = inject(Router);
  private messageService = inject(MessageService);

  username = '';
  password = '';
  loading = false;
  rememberMe = false;

  onSubmit() {
     if (!this.username || !this.password) return;

  this.loading = true;

  this.loginService.login(this.username, this.password, this.rememberMe).subscribe({ // Updated method call
    next: () => {
      this.loading = false;
      this.router.navigate(['/cars']);
    },
    error: (err) => {
      this.loading = false;
      this.messageService.showError(err);
    },
  });
}
}
