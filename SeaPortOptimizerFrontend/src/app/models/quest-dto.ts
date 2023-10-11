import {ResourceDto} from "./resource-dto";
import {QuestPrototypeDto} from "./quest-prototype-dto";
import {GuidGenerator} from "../utilities/guid-generator";

export class QuestDto extends QuestPrototypeDto{
  id: string;


  constructor(name: string, id: string, isActive: boolean, resource: string, itemsPerCapacity: number, demand: number) {
    super(name, isActive, resource, itemsPerCapacity, demand);
    this.id = id;
  }

  static fromQuestPrototypeDto(questPrototypeDto: QuestPrototypeDto): QuestDto {
    return new QuestDto(questPrototypeDto.name, GuidGenerator.newGuidV4(), questPrototypeDto.isActive, questPrototypeDto.resource, questPrototypeDto.itemsPerCapacity, questPrototypeDto.demand);
  }
}
