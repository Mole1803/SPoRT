import {ModelBaseDto} from "./model-base-dto";

export class ShipPrototypeDto extends ModelBaseDto {

  capacity: number;

  isActive: boolean;

  constructor(name: string, capacity: number, isActive: boolean) {
    super(name);
    this.capacity = capacity;
    this.isActive = isActive;
  }

}
