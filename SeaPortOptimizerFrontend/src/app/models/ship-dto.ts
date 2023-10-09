import {ShipPrototypeDto} from "./ship-prototype-dto";
import {GuidGenerator} from "../utilities/guid-generator";

export class ShipDto implements ShipPrototypeDto {
  name: string;
  capacity: number;
  id: string;
  isActive: boolean;

  constructor(id: string,name: string, capacity: number, isActive: boolean) {
    this.name = name;
    this.capacity = capacity;
    this.id = id;
    this.isActive = isActive;
  }

  static fromShipPrototypeDto(shipPrototypeDto: ShipPrototypeDto): ShipDto {
    return new ShipDto(GuidGenerator.newGuidV4(), shipPrototypeDto.name, shipPrototypeDto.capacity, shipPrototypeDto.isActive);

  }
}
