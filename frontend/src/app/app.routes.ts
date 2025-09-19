import { Routes } from '@angular/router';
import { LayoutComponent } from './core/components/layout/layout.component';
import { CarListPageComponent } from './features/car/pages/car-list-page/car-list-page.component';
import { CarDetailsComponent } from './features/car/components/car-details/car-details.component';
import { EditCarComponent } from './features/car/components/edit-car/edit-car.component';

export const routes: Routes = [
  {
    path: '',
    component: LayoutComponent, // layout wraps everything
    children: [
      { path: 'cars', component: CarListPageComponent },
      { path: 'cars/:id', component: CarDetailsComponent }, // Route with car ID
      { path: 'cars/:id/edit', component: EditCarComponent }, // Route for editing car

      /*{ path: 'cars' },
      { path: 'cars/:id', component: CarDetailComponent },
      { path: 'login', component: LoginComponent },*/
    ],
  },
];