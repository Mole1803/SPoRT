export class ShipPrototypeDto {
  name: string;
  capacity: number;

  isActive: boolean;

  constructor(name: string, capacity: number, isActive: boolean) {
    this.name = name;
    this.capacity = capacity;
    this.isActive = isActive;
  }

}
