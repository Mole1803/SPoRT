import {ShipPrototypeDto} from "./ship-prototype-dto";
import {GuidGenerator} from "../utilities/guid-generator";

export class ShipDto extends ShipPrototypeDto {

  id: string;


  constructor(id: string,name: string, capacity: number, is_active: boolean) {
    super(name, capacity, is_active)
    this.id = id;
  }

  static fromShipPrototypeDto(shipPrototypeDto: ShipPrototypeDto): ShipDto {
    return new ShipDto(GuidGenerator.newGuidV4(), shipPrototypeDto.name, shipPrototypeDto.capacity, shipPrototypeDto.is_active);

  }
}
