import {ResourceDto} from "./resource-dto";
import {QuestPrototypeDto} from "./quest-prototype-dto";
import {GuidGenerator} from "../utilities/guid-generator";

export class QuestDto {
  name: string;
  id: string;
  isActive: boolean;
  resource: string;
  itemsPerCapacity: number;
  demand: number;

  constructor(name: string, id: string, isActive: boolean, resource: string, itemsPerCapacity: number, demand: number) {
    this.name = name;
    this.id = id;
    this.isActive = isActive;
    this.resource = resource;
    this.itemsPerCapacity = itemsPerCapacity;
    this.demand = demand;
  }

  static fromQuestPrototypeDto(questPrototypeDto: QuestPrototypeDto): QuestDto {
    return new QuestDto(questPrototypeDto.name, GuidGenerator.newGuidV4(), questPrototypeDto.isActive, questPrototypeDto.resource, questPrototypeDto.itemsPerCapacity, questPrototypeDto.demand);
  }
}
