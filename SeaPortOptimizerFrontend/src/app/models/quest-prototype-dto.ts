import {ModelBaseDto} from "./model-base-dto";

export class QuestPrototypeDto extends ModelBaseDto {
  isActive: boolean;
  resource: string;
  itemsPerCapacity: number;
  demand: number;

  constructor(name: string,  isActive: boolean, resource: string, itemsPerCapacity: number, demand: number) {
    super(name);

    this.isActive = isActive;
    this.resource = resource;
    this.itemsPerCapacity = itemsPerCapacity;
    this.demand = demand;
  }
}
