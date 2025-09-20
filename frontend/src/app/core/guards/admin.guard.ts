import { CanActivateFn, Router } from '@angular/router';
import { inject } from '@angular/core';
import { AuthService } from '../services/auth.service';
import { Location } from '@angular/common';


export const adminGuard: CanActivateFn = () => {
 const authService = inject(AuthService);
  const router = inject(Router);
    const location = inject(Location);


  const token = authService.getToken();
  if (!token) {
    router.navigate(['/login']);
    return false;
  }

  const payloadBase64 = token.split('.')[1];
  if (!payloadBase64) {
    router.navigate(['/login']);
    return false;
  }

  try {
    if (!authService.isAdmin()) {
      alert('You are not allowed to access this page.');
      location.back(); // go back to the previous page
      return false;
    }

    return true; // allow all other users
  } catch (e) {
    console.error('Invalid token', e);
    router.navigate(['/login']);
    return false;
  }
};
