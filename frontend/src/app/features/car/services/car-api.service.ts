import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

export interface Car {
  id: number;
  model: { id: number; name: string };
  body_type: { id: number; name: string };
  color: string;
  doors: number;
  drive_type: { id: number; name: string };
  engine_type: { id: number; name: string };
  engine_capacity: number;
  fuel_consumption: number;
  license_plate: string;
  mileage: number;
  owner: { id: number; username: string };
  price: number;
  registration_year: number;
  transmission_type: { id: number; name: string };
  vin: string;
}

export interface PaginatedCars {
  cars: Car[];
  page: number;
  total_pages: number;
  total_items: number;
}

@Injectable({
  providedIn: 'root'
})
export class CarApiService {

   private readonly baseUrl = '/api/cars'; // Remove http://localhost:5000

    constructor(private http: HttpClient) {}

    /**
   * Get paginated list of cars
   * @param page page number (default 1)
   * @param perPage items per page (default 10)
   */
  getCars(page = 1, perPage = 10): Observable<PaginatedCars> {
    const params = new HttpParams()
      .set('page', page)
      .set('per_page', perPage);

    return this.http.get<PaginatedCars>(this.baseUrl, { params });
  }

  /**
   * Get a single car by ID
   * @param carId Car ID
   */
  getCarById(carId: number): Observable<Car> {
    const url = `${this.baseUrl}/${carId}`;
    return this.http.get<Car>(url);
  }
}
