import { Component, Input, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Car, CarApiService } from '../../services/car-api.service';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatDividerModule } from '@angular/material/divider';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-car-details',
  standalone: true,
  imports: [
    CommonModule,
    MatCardModule,
    MatButtonModule,
    MatIconModule,
    MatDividerModule
  ],
  templateUrl: './car-details.component.html',
  styleUrls: ['./car-details.component.scss']
})
export class CarDetailsComponent implements OnInit {
  carId!: number;
  car!: Car;

  constructor(private carApi: CarApiService, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.carId = Number(this.route.snapshot.paramMap.get('id'));
      const carId = Number(this.route.snapshot.paramMap.get('id'));
    console.log('Fetching details for car ID:', this.carId);
    this.carApi.getCarById(this.carId).subscribe((car: Car) => {
      this.car = car;
    });
  }
}