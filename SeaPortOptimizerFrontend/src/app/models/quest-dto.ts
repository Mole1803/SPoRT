import {ResourceDto} from "./resource-dto";

export class QuestDto {
  id: string;
  name: string;
  resource: ResourceDto;
  isActive: boolean;


  constructor(id: string, name: string, resource: ResourceDto, isActive: boolean) {
    this.id = id;
    this.name = name;
    this.resource = resource;
    this.isActive = isActive;
  }

}
