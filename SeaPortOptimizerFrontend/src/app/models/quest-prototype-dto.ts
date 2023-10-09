export class QuestPrototypeDto {
  name: string;
  isActive: boolean;
  resource: string;
  itemsPerCapacity: number;
  demand: number;

  constructor(name: string,  isActive: boolean, resource: string, itemsPerCapacity: number, demand: number) {
    this.name = name;
    this.isActive = isActive;
    this.resource = resource;
    this.itemsPerCapacity = itemsPerCapacity;
    this.demand = demand;
  }
}
