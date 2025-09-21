import { Component, OnInit, inject } from '@angular/core';
import { HasId, DropdownData, Car } from '../../../../shared/interfaces/common.interface';
import { CarApiService } from '../../services/car-api.service';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
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
  selector: 'app-create-car',
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
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
  templateUrl: './create-car.component.html',
  styleUrl: './create-car.component.scss'
})
export class CreateCarComponent implements OnInit {
  private carApi = inject(CarApiService);
  private router = inject(Router);
  private messageService = inject(MessageService);
  private fb = inject(FormBuilder);

  carForm!: FormGroup;

  models: { id: number; name: string }[] = [];
  bodyTypes: { id: number; name: string }[] = [];
  transmissionTypes: { id: number; name: string }[] = [];
  driveTypes: { id: number; name: string }[] = [];
  engineTypes: { id: number; name: string }[] = [];
  owners: { id: number; username: string }[] = [];
  colors: string[] = ['Red', 'Blue', 'Black', 'White', 'Silver', 'Green'];
  saving = false;

  ngOnInit(): void {
    this.loadDropdownsAndCar();
    this.carForm = this.fb.group({
      model: [null, Validators.required],
      body_type: [null, Validators.required],
      transmission_type: [null, Validators.required],
      drive_type: [null, Validators.required],
      engine_type: [null, Validators.required],
      owner: [null, Validators.required],
      color: ['', Validators.required],
      mileage: [0, [Validators.required, Validators.min(1)]],
      doors: [0, [Validators.required, Validators.min(1)]],
      engine_capacity: [0, [Validators.required, Validators.min(0.1)]],
      fuel_consumption: [0, [Validators.required, Validators.min(0.1)]],
      license_plate: ['', Validators.required],
      vin: ['', Validators.required],
      registration_year: [new Date().getFullYear(), [Validators.required, Validators.min(1900)]],
      price: [0, [Validators.required, Validators.min(1)]]
    });
  }

  /** Compare function for object selects */
  compareById(obj1: HasId, obj2: HasId): boolean {
    return obj1 && obj2 ? obj1.id === obj2.id : obj1 === obj2;
  }

  /** Load all dropdowns */
  loadDropdownsAndCar() {
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
      engineTypes: this.carApi.getEngineTypes().pipe(catchError((error: HttpErrorResponse) => {
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
        this.engineTypes = Array.isArray(res.engineTypes) ? res.engineTypes : res.engineTypes?.engine_types ?? [];
        this.owners = Array.isArray(res.owners) ? res.owners : res.owners?.owners ?? [];
      },
      error: (err) => this.messageService.showError(err)
    });
  }

  saveCar() {
    if (this.carForm.invalid) {
      this.messageService.showError('Please fill in all required fields.');
      return;
    }
    this.saving = true;
    this.carApi.createCar(this.carForm.value).subscribe({ 
      next: () => {
        this.saving = false;
        this.messageService.showSuccess('Car created successfully!'); 
        this.router.navigate(['/cars']);
      },
      error: (err) => {
        this.saving = false;
        this.messageService.showError(err);
      }
    });
  }
}
