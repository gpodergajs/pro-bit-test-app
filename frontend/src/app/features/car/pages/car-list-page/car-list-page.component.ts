import { Component, OnInit } from '@angular/core';
import { CarApiService, Car } from '../../services/car-api.service';
import { Observable, of } from 'rxjs';
import { catchError, map } from 'rxjs/operators';
import { CommonModule } from '@angular/common';
import { CarDataViewComponent } from '../../components/car-data-view/car-data-view.component';

@Component({
  selector: 'app-car-list-page',
  standalone: true,
  imports: [CommonModule, CarDataViewComponent],
  templateUrl: './car-list-page.component.html',
  styleUrl: './car-list-page.component.scss'
})
export class CarListPageComponent implements OnInit {
  cars$: Observable<Car[]> = of([]);

  constructor(private carApi: CarApiService) { }

  ngOnInit(): void {
    this.cars$ = this.carApi.getCars(1, 10).pipe(
      map(response => response.cars),
      catchError(error => {
        console.error('Error fetching cars:', error);
        return of([]); // Return an empty array on error
      })
    );
  }
}

