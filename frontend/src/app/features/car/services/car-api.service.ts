import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of, tap } from 'rxjs';

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

  // Caches
  private transmissionCache: any[] | null = null;
  private driveCache: any[] | null = null;
  private ownerCache: any[] | null = null;
  private bodyCache: any[] | null = null;
  private modelCache: any[] | null = null;
  private colorCache: string[] | null = null;

   private readonly baseUrl = '/api/cars'; // Remove http://localhost:5000

    constructor(private http: HttpClient) {}

    /**
   * Get paginated list of cars
   * @param page page number (default 1)
   * @param perPage items per page (default 10)
   * @param filterField The field to filter by (e.g., 'model', 'color')
   * @param filterValue The value to filter for
   */
 getCars(
  page = 1,
  perPage = 10,
  filters?: { priceFrom?: number; priceTo?: number; mileage?: number; year?: number }
): Observable<PaginatedCars> {
  let params = new HttpParams()
    .set('page', page)
    .set('per_page', perPage);

  if (filters) {
    if (filters.priceFrom != null) {
      params = params.set('price_from', filters.priceFrom.toString());
    }
    if (filters.priceTo != null) {
      params = params.set('price_to', filters.priceTo.toString());
    }
    if (filters.mileage != null) {
      params = params.set('mileage', filters.mileage.toString());
    }
    if (filters.year != null) {
      params = params.set('year', filters.year.toString());
    }
  }

  return this.http.get<PaginatedCars>(this.baseUrl, { params });
}


  /**
 * Get a single car by ID
 * @param carId Car ID
 */
getCarById(carId: number): Observable<Car> {
  const url = `${this.baseUrl}/${carId}`;
    console.log('Fetching car with ID:', carId, 'URL:', url); // optional debug
    return this.http.get<any>(url);
  }

  updateCar(carId: number, car: Car): Observable<Car> {
  return this.http.put<Car>(`/api/cars/${carId}`, car);
}

  /** Dropdown services with caching */

  getTransmissionTypes(): Observable<any[]> {
    if (this.transmissionCache) return of(this.transmissionCache);
    return this.http.get<any[]>(`${this.baseUrl}/transmissions`).pipe(
      tap(data => this.transmissionCache = data)
    );
  }

  getDriveTypes(): Observable<any[]> {
    if (this.driveCache) return of(this.driveCache);
    return this.http.get<any[]>(`${this.baseUrl}/drives`).pipe(
      tap(data => this.driveCache = data)
    );
  }

  getOwners(): Observable<any[]> {
    if (this.ownerCache) return of(this.ownerCache);
    return this.http.get<any[]>(`${this.baseUrl}/owners`).pipe(
      tap(data => this.ownerCache = data)
    );
  }

  getBodyTypes(): Observable<any[]> {
    if (this.bodyCache) return of(this.bodyCache);
    return this.http.get<any[]>(`${this.baseUrl}/bodies`).pipe(
      tap(data => this.bodyCache = data)
    );
  }

  getModels(): Observable<any[]> {
    if (this.modelCache) return of(this.modelCache);
    return this.http.get<any[]>(`${this.baseUrl}/models`).pipe(
      tap(data => this.modelCache = data)
    );
  }

  getColors(): Observable<string[]> {
    if (this.colorCache) return of(this.colorCache);
    return this.http.get<string[]>(`${this.baseUrl}/colors`).pipe(
      tap(data => this.colorCache = data)
    );
  }
}

