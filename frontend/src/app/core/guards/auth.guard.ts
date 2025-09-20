import { CanActivateFn, Router } from '@angular/router';
import { AuthService } from '../../features/auth/services/auth.service';
import { inject } from '@angular/core';

export const authGuard: CanActivateFn = (route, state) => {
  const authService = inject(AuthService);
  const router = inject(Router);
  console.log(authService.isLoggedIn())
  if (authService.isLoggedIn()) {
    console.log('logged in')
    return true;
  } else {
    // Redirect to login if token is missing or expired
    return router.parseUrl('/login');
  }
};
