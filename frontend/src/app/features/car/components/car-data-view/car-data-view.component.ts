import { PageEvent } from "@angular/material/paginator";
import { Car, CarApiService } from "../../services/car-api.service";
import { Component, Input, OnInit } from "@angular/core";
import { CommonModule } from "@angular/common";
import { MatButtonModule } from "@angular/material/button";
import { MatFormFieldModule } from "@angular/material/form-field";
import { MatInputModule } from "@angular/material/input";
import { MatSelectModule } from "@angular/material/select";
import { PaginatorComponent } from "../../../../shared/components/paginator/paginator.component";
import { MatCardModule } from "@angular/material/card";
import { MatAutocompleteModule } from "@angular/material/autocomplete";
import { FormsModule } from "@angular/forms";
// If you are no longer using <app-filter>, remove FilterComponent
// import { FilterComponent } from "../../../../shared/components/filter/filter.component";

@Component({
  selector: 'app-car-data-view',
  standalone: true,
  imports: [
    CommonModule,
    MatCardModule,
    MatButtonModule,
    // If you are no longer using <app-filter>, remove FilterComponent
    // FilterComponent,
    PaginatorComponent,

    // Angular Material form controls
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    MatAutocompleteModule,
    FormsModule
  ],
  templateUrl: './car-data-view.component.html',  
  styleUrls: ['./car-data-view.component.scss']
})
export class CarDataViewComponent implements OnInit {
  @Input() cars: Car[] = [];

  layout: string = 'grid';
  options = ['list', 'grid'];

  // Pagination properties
  totalCars = 0;
  pageSize = 10;
  pageIndex = 0;
  pageSizeOptions = [5, 10, 25, 100];

  // Filter property
  filters = {
    priceFrom: null,
    priceTo: null,
    mileage: null,
    year: null
  };

  years: number[] = [];
  filteredYears: number[] = [];

  constructor(private carApi: CarApiService) {}

  ngOnInit(): void {
    const currentYear = new Date().getFullYear();
    this.years = Array.from({ length: 30 }, (_, i) => currentYear - i); // last 30 years
    this.filteredYears = [...this.years];
  }

  onPageChange(event: PageEvent) {
    this.pageIndex = event.pageIndex;
    this.pageSize = event.pageSize;
  }

  applyFilter() {
    console.log('Filters applied:', this.filters);
    // TODO: call API with this.filters and update `this.cars`
  }

  clearFilter() {
    this.filters = { priceFrom: null, priceTo: null, mileage: null, year: null };
    this.filteredYears = [...this.years];
    console.log('Filters cleared');
    // TODO: reload all cars
  }
}
