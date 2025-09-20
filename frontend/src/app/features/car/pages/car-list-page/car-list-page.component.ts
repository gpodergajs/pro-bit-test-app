import { Component, OnInit, inject } from '@angular/core';
import { PageEvent } from '@angular/material/paginator';
import { CarApiService, Car } from '../../services/car-api.service';
import { Observable, of } from 'rxjs';
import { catchError, map, finalize, delay } from 'rxjs/operators';
import { CommonModule } from '@angular/common';
import { CarDataViewComponent } from '../../components/car-data-view/car-data-view.component';
import { FormBuilder, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { PaginatorComponent } from '../../../../shared/components/paginator/paginator.component';
import { ProgressBarComponent } from '../../../../shared/components/progress-bar/progress-bar.component';

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

    ReactiveFormsModule,
    ProgressBarComponent,
  ],
  templateUrl: './car-list-page.component.html',
  styleUrl: './car-list-page.component.scss'
})
export class CarListPageComponent implements OnInit {
  private carApi = inject(CarApiService);
  private fb = inject(FormBuilder);

  cars$: Observable<Car[]> = of([]);

  isGridView = false;
  loading = false;
  // Pagination properties
  totalCars = 0;
  pageSize = 10;
  pageIndex = 0;
  pageSizeOptions = [5, 10, 25, 50];

  // Filters
  filterForm!: FormGroup;

  priceOptions = [5000, 10000, 15000, 20000, 30000, 50000];
  mileageOptions = [5000, 10000, 20000, 50000, 100000, 150000, 200000, 2500000];
  years: number[] = [];

  ngOnInit(): void {
    const currentYear = new Date().getFullYear();
    this.years = Array.from({ length: 30 }, (_, i) => currentYear - i);

    this.filterForm = this.fb.group({
      priceFrom: [undefined],
      priceTo: [undefined],
      mileageTo: [undefined],
      yearFrom: [undefined],
      yearTo: [undefined]
    }, { validators: this.priceAndYearValidator });

    // Load first page
    this.loadCars();
  }

  private priceAndYearValidator(form: FormGroup) {
    const priceFromControl = form.get('priceFrom');
    const priceToControl = form.get('priceTo');
    const yearFromControl = form.get('yearFrom');
    const yearToControl = form.get('yearTo');

    const priceFrom = priceFromControl?.value;
    const priceTo = priceToControl?.value;
    const yearFrom = yearFromControl?.value;
    const yearTo = yearToControl?.value;

    // Price validation
    if (priceFrom !== null && priceFrom !== undefined && priceFrom !== '' &&
        priceTo !== null && priceTo !== undefined && priceTo !== '') {
      if (priceFrom >= priceTo) {
        priceToControl?.setErrors({ priceToLessThanPriceFrom: true });
      } else {
        priceToControl?.setErrors(null);
      }
    } else {
      priceToControl?.setErrors(null); // Clear error if one or both are empty
    }

    // Year validation
    if (yearFrom !== null && yearFrom !== undefined && yearFrom !== '' &&
        yearTo !== null && yearTo !== undefined && yearTo !== '') {
      if (yearFrom >= yearTo) {
        yearToControl?.setErrors({ yearToLessThanYearFrom: true });
      } else {
        yearToControl?.setErrors(null);
      }
    } else {
      yearToControl?.setErrors(null); // Clear error if one or both are empty
    }

    return null;
  }

  loadCars() {
    this.loading = true;
    this.cars$ = this.carApi.getCars(this.pageIndex + 1, this.pageSize, this.filterForm.value).pipe(
      map(response => {
        this.totalCars = response.total_items; // Update totalCars for paginator
        return response.cars;
      }),
      catchError(err => {
        console.error('Error fetching cars:', err);
        return of([]);
      }),
      finalize(() => this.loading = false)
    );
  }

  applyFilter() {
    if (this.filterForm.invalid) {
      return;
    }
    this.pageIndex = 0; // Reset to first page when filters change
    this.loadCars();
    console.log('Filters applied:', this.filterForm.value);
  }

  clearFilter() {
    this.filterForm.reset();
    this.pageIndex = 0;
    this.loadCars();
  }

  onPageChange(event: PageEvent) {
    this.pageIndex = event.pageIndex;
    this.pageSize = event.pageSize;
    this.loadCars();
  }


  handleCarDelete(carId:number) {
     this.carApi.deleteCar(carId).subscribe(success => {
    if (success) {
      console.log(`Car ${carId} deleted`);
      this.loadCars(); // refresh list
    } else {
      console.error('Failed to delete car');
    }
  });
  }


}


