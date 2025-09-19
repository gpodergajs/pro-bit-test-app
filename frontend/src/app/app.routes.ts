import { Routes } from '@angular/router';
import { LayoutComponent } from './core/components/layout/layout.component';
import { CarListPageComponent } from './features/car/pages/car-list-page/car-list-page.component';
import { CarDetailsComponent } from './features/car/components/car-details/car-details.component';
import { EditCarComponent } from './features/car/components/edit-car/edit-car.component';
import { LoginPageComponent } from './features/auth/pages/login-page/login-page.component';
import { authGuard } from './core/guards/auth.guard';
import { adminGuard } from './core/guards/admin.guard';

export const routes: Routes = [
  {
    path: '',
    component: LayoutComponent, // layout wraps everything
    children: [
      { path: 'cars', component: CarListPageComponent },
      { path: 'cars/:id', component: CarDetailsComponent, canActivate: [authGuard] }, // Route with car ID
      { path: 'cars/:id/edit', component: EditCarComponent, canActivate: [authGuard, adminGuard] }, // Route for editing car
      { path: 'login', component: LoginPageComponent }
      /*{ path: 'cars' },
      { path: 'cars/:id', component: CarDetailComponent },
      { path: 'login', component: LoginComponent },*/
    ],
  },
];