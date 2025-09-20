import { Component, OnInit, inject } from '@angular/core';
import { HasId, DropdownData, Car } from '../../../../shared/interfaces/common.interface';
import { CarApiService } from '../../services/car-api.service';
import { ActivatedRoute, Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatDividerModule } from '@angular/material/divider';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { forkJoin, of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { HttpErrorResponse } from '@angular/common/http';
import { ProgressBarComponent } from '../../../../shared/components/progress-bar/progress-bar.component';
import { MessageService } from '../../../../core/services/message.service';


@Component({
  selector: 'app-edit-car',
  imports: [
    CommonModule,
    FormsModule,
    MatCardModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatDividerModule,
    MatIconModule,
    MatSelectModule,
    ProgressBarComponent
  ],
  standalone: true,
  templateUrl: './edit-car.component.html',
  styleUrl: './edit-car.component.scss'
})
export class EditCarComponent implements OnInit {
  private route = inject(ActivatedRoute);
  private carApi = inject(CarApiService);
  private router = inject(Router);
  private messageService = inject(MessageService);

  car!: Car;

  models: { id: number; name: string }[] = [];
  bodyTypes: { id: number; name: string }[] = [];
  transmissionTypes: { id: number; name: string }[] = [];
  driveTypes: { id: number; name: string }[] = [];
  owners: { id: number; username: string }[] = [];
  colors: string[] = ['Red', 'Blue', 'Black', 'White', 'Silver', 'Green'];
  saving = false;

  ngOnInit(): void {
    const carId = Number(this.route.snapshot.paramMap.get('id'));
    if (carId) {
      this.loadDropdownsAndCar(carId);
    }
  }

  /** Compare function for object selects */
  compareById(obj1: HasId, obj2: HasId): boolean {
    return obj1 && obj2 ? obj1.id === obj2.id : obj1 === obj2;
  }

  /** Load all dropdowns first, then the car */
  loadDropdownsAndCar(carId: number) {
    forkJoin({
      models: this.carApi.getModels().pipe(catchError((error: HttpErrorResponse) => {
        this.messageService.showError(error);
        return of([]);
      })),
      bodyTypes: this.carApi.getBodyTypes().pipe(catchError((error: HttpErrorResponse) => {
        this.messageService.showError(error);
        return of([]);
      })),
      transmissionTypes: this.carApi.getTransmissionTypes().pipe(catchError((error: HttpErrorResponse) => {
        this.messageService.showError(error);
        return of([]);
      })),
      driveTypes: this.carApi.getDriveTypes().pipe(catchError((error: HttpErrorResponse) => {
        this.messageService.showError(error);
        return of([]);
      })),
      owners: this.carApi.getOwners().pipe(catchError((error: HttpErrorResponse) => {
        this.messageService.showError(error);
        return of([]);
      }))
    }).subscribe({
      next: (res: DropdownData) => {
        this.models = Array.isArray(res.models) ? res.models : res.models?.models ?? [];
        this.bodyTypes = Array.isArray(res.bodyTypes) ? res.bodyTypes : res.bodyTypes?.body_types ?? [];
        this.transmissionTypes = Array.isArray(res.transmissionTypes)
          ? res.transmissionTypes
          : res.transmissionTypes?.transmission_types ?? [];
        this.driveTypes = Array.isArray(res.driveTypes) ? res.driveTypes : res.driveTypes?.drive_types ?? [];
        this.owners = Array.isArray(res.owners) ? res.owners : res.owners?.owners ?? [];

        this.loadCar(carId);
      },
      error: (err) => this.messageService.showError(err)
    });
  }

  loadCar(carId: number) {
    this.carApi.getCarById(carId).subscribe({
      next: (car) => this.car = car,
      error: (err) => this.messageService.showError(err)
    });
  }

 saveCar() {
    if (!this.car) return;
    this.saving = true;
    this.carApi.updateCar(this.car.id, this.car).subscribe({
      next: () => {
        this.saving = false;
        this.messageService.showSuccess('Car saved successfully!');
        this.router.navigate(['/cars']); 
      },
      error: (err) => {
        this.saving = false;
        this.messageService.showError(err);
      }
    });
  }
}