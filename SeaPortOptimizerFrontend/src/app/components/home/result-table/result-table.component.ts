import {Component, Input} from '@angular/core';
import {Result} from "../../../models/result";
import {ShipDto} from "../../../models/ship-dto";
import {QuestDto} from "../../../models/quest-dto";

@Component({
  selector: 'app-result-table',
  templateUrl: './result-table.component.html',
  styleUrls: ['./result-table.component.css']
})
export class ResultTableComponent {
  @Input() result?: Result;
  @Input() shipDto?: ShipDto[];
  @Input() questDto?: QuestDto[];

  mapIdToShip(id: string): string {
    if(this.shipDto===undefined) return "";
    return this.shipDto.find(ship => ship.id === id)?.name as string;
  }

  mapIdToQuest(id: string): string {
    if(this.questDto===undefined) return "";
    return this.questDto.find(quest => quest.id === id)?.name as string;
  }


  protected readonly Result = Result;
}
