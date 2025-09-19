import { Routes } from '@angular/router';
import { LayoutComponent } from './core/components/layout/layout.component';
import { CarListPageComponent } from './features/car/pages/car-list-page/car-list-page.component';


export const routes: Routes = [
  {
    path: '',
    component: LayoutComponent, // layout wraps everything
    children: [
      { path: 'cars', component: CarListPageComponent },
      /*{ path: 'cars' },
      { path: 'cars/:id', component: CarDetailComponent },
      { path: 'login', component: LoginComponent },*/
    ],
  },
];