import { Routes } from '@angular/router';
import { LayoutComponent } from './core/components/layout/layout.component';
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
        path: 'cars/create',
        loadComponent: () =>
          import('./features/car/components/create-car/create-car.component')
            .then((m) => m.CreateCarComponent),
        canActivate: [authGuard, adminGuard],
      },
      {
        path: 'cars/edit/:id',
        loadComponent: () =>
          import('./features/car/components/edit-car/edit-car.component')
            .then((m) => m.EditCarComponent),
        canActivate: [authGuard, adminGuard],
      },
      {
        path: 'cars/:id',
        loadComponent: () =>
          import('./features/car/components/car-details/car-details.component')
            .then((m) => m.CarDetailsComponent),
        canActivate: [],
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