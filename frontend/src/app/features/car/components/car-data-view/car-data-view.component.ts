import { CarApiService } from "../../services/car-api.service";
import { Car } from "../../../../shared/interfaces/common.interface";
import { Component, EventEmitter, Input, OnInit, Output, inject } from "@angular/core";
import { CommonModule } from "@angular/common";
import { MatButtonModule } from "@angular/material/button";
import { MatFormFieldModule } from "@angular/material/form-field";
import { MatInputModule } from "@angular/material/input";
import { MatSelectModule } from "@angular/material/select";
import { MatCardModule } from "@angular/material/card";
import { MatAutocompleteModule } from "@angular/material/autocomplete";
import { FormsModule } from "@angular/forms";
import { Router, RouterLink } from "@angular/router";
import { MatGridListModule } from '@angular/material/grid-list';
import { AuthService } from "../../../../core/services/auth.service";


@Component({
  selector: 'app-car-data-view',
  standalone: true,
  imports: [
    CommonModule,
    MatCardModule,
    MatButtonModule,
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    MatAutocompleteModule,
    FormsModule,
    RouterLink,
    MatGridListModule
  ],
  templateUrl: './car-data-view.component.html',  
  styleUrls: ['./car-data-view.component.scss']
})
export class CarDataViewComponent implements OnInit {
  authService = inject(AuthService);
  carService = inject(CarApiService)
  router = inject(Router)

  @Input() cars: Car[] = [];
  @Output() deleteCar = new EventEmitter<number>(); 

  isAdmin = false;

  ngOnInit(): void {
    this.isAdmin = this.authService.isAdmin();
  }

  goToDetails(id: number) {
    this.router.navigate(['/cars', id]);
  }

  onCarDelete(id:number) {
    this.deleteCar.emit(id)
  }
  
}