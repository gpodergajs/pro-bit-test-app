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