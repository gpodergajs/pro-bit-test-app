import { Routes } from '@angular/router';
import { LayoutComponent } from './shared/components/layout/layout.component';

export const routes: Routes = [
  {
    path: '',
    //component: LayoutComponent, // layout wraps everything
    children: [
      /*{ path: 'cars' },
      { path: 'cars/:id', component: CarDetailComponent },
      { path: 'login', component: LoginComponent },*/
    ],
  },
];