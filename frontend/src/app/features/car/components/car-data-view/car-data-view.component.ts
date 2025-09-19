import { Component, Input } from '@angular/core';
import { Car, CarApiService } from '../../services/car-api.service';

import { CommonModule } from '@angular/common';
import { catchError, map, of } from 'rxjs';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-car-data-view',
  standalone: true,
  imports: [CommonModule, MatCardModule, MatButtonModule],
  templateUrl: './car-data-view.component.html',  
  styleUrls: ['./car-data-view.component.scss']
})
export class CarDataViewComponent {
    @Input() cars: Car[] = [];

    layout: string = 'grid';
    options = ['list', 'grid'];
    rows: number = 5;
    first: number = 0;
constructor(private carApi: CarApiService ) {}

ngOnInit() {
  /*this.carApi.getCars(1, 10).pipe(
    map(response => response.cars), // extract the cars array
    catchError(error => {
      console.error('Error fetching cars:', error);
      return of([]); // Return empty array on error
    })
  ).subscribe(cars => {
    this.cars = cars;
    console.log('Cars loaded:', this.cars); // confirm data is here
  });*/
}

  onPageChange(event: any) {
    this.first = event.first;
    this.rows = event.rows;
  }
}