import { Component } from '@angular/core';
import { Car, CarApiService } from '../../services/car-api.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-edit-car',
  imports: [],
  templateUrl: './edit-car.component.html',
  styleUrl: './edit-car.component.scss'
})
export class EditCarComponent {
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
