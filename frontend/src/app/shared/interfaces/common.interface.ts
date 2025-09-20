export interface HasId {
  id: number;
}

export interface HasIdAndName extends HasId {
  name: string;
}

export interface Owner extends HasId {
  username: string;
}

export interface DropdownData {
  models: HasIdAndName[] | { models: HasIdAndName[] };
  bodyTypes: HasIdAndName[] | { body_types: HasIdAndName[] };
  transmissionTypes: HasIdAndName[] | { transmission_types: HasIdAndName[] };
  driveTypes: HasIdAndName[] | { drive_types: HasIdAndName[] };
  owners: Owner[] | { owners: Owner[] };
}

export interface TokenPayload {
  exp: number;
  user_type_id?: number;
  user_type?: number;
}

export interface LoginResponse {
  access_token: string; // JWT token returned by backend
}

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

export interface BodyType {
  id: number;
  name: string;
}

export interface Model {
  id: number;
  name: string;
}
