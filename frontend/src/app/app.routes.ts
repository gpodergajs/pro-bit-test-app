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
    component: LayoutComponent,
    children: [
      {
        path: 'cars',
        loadComponent: () =>
          import('./features/car/pages/car-list-page/car-list-page.component')
            .then((m) => m.CarListPageComponent),
      },
      {
        path: 'cars/:id',
        loadComponent: () =>
          import('./features/car/components/car-details/car-details.component')
            .then((m) => m.CarDetailsComponent),
        canActivate: [authGuard],
      },
      {
        path: 'cars/edit/:id',
        loadComponent: () =>
          import('./features/car/components/edit-car/edit-car.component')
            .then((m) => m.EditCarComponent),
        canActivate: [authGuard, adminGuard],
      },
      {
        path: 'login',
        loadComponent: () =>
          import('./features/auth/pages/login-page/login-page.component')
            .then((m) => m.LoginPageComponent),
      },
    ],
  },
];