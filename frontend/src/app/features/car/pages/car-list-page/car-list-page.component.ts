import { Component, OnInit } from '@angular/core';
import { CarApiService, Car } from '../../services/car-api.service';
import { Observable, of } from 'rxjs';
import { catchError, map } from 'rxjs/operators';
import { CommonModule } from '@angular/common';
import { CarDataViewComponent } from '../../components/car-data-view/car-data-view.component';
import { FormsModule } from '@angular/forms';
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { PaginatorComponent } from '../../../../shared/components/paginator/paginator.component';

@Component({
  selector: 'app-car-list-page',
  standalone: true,
  imports: [CommonModule, CommonModule,
    MatCardModule,
    MatButtonModule,
    PaginatorComponent,
    CarDataViewComponent,
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    MatAutocompleteModule,
    FormsModule,
  ],
  templateUrl: './car-list-page.component.html',
  styleUrl: './car-list-page.component.scss'
})
export class CarListPageComponent implements OnInit {
  cars$: Observable<Car[]> = of([]);

  isGridView = false;
  // Pagination properties
  totalCars = 0;
  pageSize = 10;
  pageIndex = 0;
  pageSizeOptions = [5, 10, 25, 50];

  // Filters
  filters: { priceFrom?: number; priceTo?: number; mileageTo?: number; yearFrom?: number; yearTo?: number } = {
    priceFrom: undefined,
    priceTo: undefined,
    mileageTo: undefined,
    yearFrom: undefined,
    yearTo: undefined
  };


  priceOptions = [5000, 10000, 15000, 20000, 30000, 50000];
  mileageOptions = [5000, 10000, 20000, 50000, 100000, 150000, 200000, 2500000];
  years: number[] = [];

  constructor(private carApi: CarApiService) { }

  ngOnInit(): void {
    const currentYear = new Date().getFullYear();
    this.years = Array.from({ length: 30 }, (_, i) => currentYear - i);

    // Load first page
    this.loadCars();
  }

  loadCars() {
    this.cars$ = this.carApi.getCars(this.pageIndex + 1, this.pageSize, this.filters).pipe(
      map(response => {
        this.totalCars = response.total_items; // Update totalCars for paginator
        return response.cars;
      }),
      catchError(err => {
        console.error('Error fetching cars:', err);
        return of([]);
      })
    );
  }

  applyFilter() {
    this.pageIndex = 0; // Reset to first page when filters change
    this.loadCars();
    console.log('Filters applied:', this.filters);
  }

  clearFilter() {
    this.filters = {
      priceFrom: undefined,
      priceTo: undefined,
      mileageTo: undefined,
      yearFrom: undefined,
      yearTo: undefined
    };
    this.pageIndex = 0;
    this.loadCars();
  }

  onPageChange(event: any) {
    this.pageIndex = event.pageIndex;
    this.pageSize = event.pageSize;
    this.loadCars();
  }



}


