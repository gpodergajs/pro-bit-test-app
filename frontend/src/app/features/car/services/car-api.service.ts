import { HttpClient, HttpErrorResponse, HttpParams } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { catchError, map, Observable, of, tap } from 'rxjs';
import { MessageService } from '../../../core/services/message.service'; // Import MessageService

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

export interface Transmission {
  id: number;
  name: string;
}

export interface Drive {
  id: number;
  name: string;
}

export interface Owner {
  id: number;
  username: string;
}

export interface BodyType {
  id: number;
  name: string;
}

export interface Model {
  id: number;
  name: string;
}

@Injectable({
  providedIn: 'root'
})
export class CarApiService {
  private http = inject(HttpClient);
  private messageService = inject(MessageService); // Inject MessageService


  // Caches
  private transmissionCache: Transmission[] | null = null;
  private driveCache: Drive[] | null = null;
  private ownerCache: Owner[] | null = null;
  private bodyCache: BodyType[] | null = null;
  private modelCache: Model[] | null = null;
  private colorCache: string[] | null = null;

   private readonly baseUrl = '/api/cars';

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
  filters?: { priceFrom?: number; priceTo?: number; mileageTo?: number; yearFrom?: number, yearTo?: number }
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
    if (filters.mileageTo != null) {
      params = params.set('mileage_to', filters.mileageTo.toString());
    }
    if (filters.yearFrom != null) {
      params = params.set('year_from', filters.yearFrom.toString());
    }
    if (filters.yearTo != null) {
      params = params.set('year_to', filters.yearTo.toString());
    }
  }

  return this.http.get<PaginatedCars>(this.baseUrl, { params });
}


 deleteCar(carId: number): Observable<boolean> {
  return this.http.delete(`/api/cars/${carId}`, { observe: 'response' }).pipe(
    map(response => response.status === 200),
    catchError((error: HttpErrorResponse) => {
      this.messageService.showError(error);
      return of(false);
    })               
  );
}

  /**
 * Get a single car by ID
 * @param carId Car ID
 */
getCarById(carId: number): Observable<Car> {
  const url = `${this.baseUrl}/${carId}`;
    
    return this.http.get<Car>(url);
  }

  updateCar(carId: number, car: Car): Observable<Car> {
  return this.http.put<Car>(`/api/cars/${carId}`, car);
}

  /** Dropdown services with caching */

  getTransmissionTypes(): Observable<Transmission[]> {
    if (this.transmissionCache) return of(this.transmissionCache);
    return this.http.get<Transmission[]>(`${this.baseUrl}/transmissions`).pipe(
      tap(data => this.transmissionCache = data)
    );
  }

  getDriveTypes(): Observable<Drive[]> {
    if (this.driveCache) return of(this.driveCache);
    return this.http.get<Drive[]>(`${this.baseUrl}/drives`).pipe(
      tap(data => this.driveCache = data)
    );
  }

  getOwners(): Observable<Owner[]> {
    if (this.ownerCache) return of(this.ownerCache);
    return this.http.get<Owner[]>(`${this.baseUrl}/owners`).pipe(
      tap(data => this.ownerCache = data)
    );
  }

  getBodyTypes(): Observable<BodyType[]> {
    if (this.bodyCache) return of(this.bodyCache);
    return this.http.get<BodyType[]>(`${this.baseUrl}/bodies`).pipe(
      tap(data => this.bodyCache = data)
    );
  }

  getModels(): Observable<Model[]> {
    if (this.modelCache) return of(this.modelCache);
    return this.http.get<Model[]>(`${this.baseUrl}/models`).pipe(
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