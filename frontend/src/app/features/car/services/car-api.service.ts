import { HttpClient, HttpErrorResponse, HttpParams } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { catchError, map, Observable, of, tap } from 'rxjs';
import { MessageService } from '../../../core/services/message.service';
import { Car, PaginatedCars, Transmission, Drive, Owner, BodyType, Model, CarUpdatePayload } from '../../../shared/interfaces/common.interface';

@Injectable({
  providedIn: 'root'
})
export class CarApiService {
  private http = inject(HttpClient);
  private messageService = inject(MessageService);


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
    const payload: CarUpdatePayload = {
      vin: car.vin,
      license_plate: car.license_plate,
      model_id: car.model.id,
      owner_id: car.owner.id,
      body_type_id: car.body_type.id,
      engine_type_id: car.engine_type.id,
      transmission_type_id: car.transmission_type.id,
      drive_type_id: car.drive_type.id,
      engine_capacity: car.engine_capacity,
      fuel_consumption: car.fuel_consumption,
      mileage: car.mileage,
      color: car.color,
      doors: car.doors,
      registration_year: car.registration_year,
      price: car.price,
    };
    return this.http.put<Car>(`/api/cars/${carId}`, payload);
  }

  createCar(car: Car): Observable<Car> {
    const payload: CarUpdatePayload = {
      vin: car.vin,
      license_plate: car.license_plate,
      model_id: car.model.id,
      owner_id: car.owner.id,
      body_type_id: car.body_type.id,
      engine_type_id: car.engine_type.id,
      transmission_type_id: car.transmission_type.id,
      drive_type_id: car.drive_type.id,
      engine_capacity: car.engine_capacity,
      fuel_consumption: car.fuel_consumption,
      mileage: car.mileage,
      color: car.color,
      doors: car.doors,
      registration_year: car.registration_year,
      price: car.price,
    };
    return this.http.post<Car>(this.baseUrl, payload);
  }

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

  getEngineTypes(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/engines`);
  }

  getColors(): Observable<string[]> {
    if (this.colorCache) return of(this.colorCache);
    return this.http.get<string[]>(`${this.baseUrl}/colors`).pipe(
      tap(data => this.colorCache = data)
    );
  }
}