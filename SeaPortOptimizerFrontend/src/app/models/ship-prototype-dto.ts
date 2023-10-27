import {ModelBaseDto} from "./model-base-dto";

export class ShipPrototypeDto extends ModelBaseDto {

  capacity: number;

  is_active: boolean;

  constructor(name: string, capacity: number, is_active: boolean) {
    super(name);
    this.capacity = capacity;
    this.is_active = is_active;
  }

}
