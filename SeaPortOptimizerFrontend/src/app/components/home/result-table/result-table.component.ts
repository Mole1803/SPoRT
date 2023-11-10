import {Component, Input} from '@angular/core';
import {Result} from "../../../models/result";
import {ShipDto} from "../../../models/ship-dto";
import {QuestDto} from "../../../models/quest-dto";
import {HomeComponent} from "../../../views/home/home.component";
import {ResultHttpRequestService} from "../../../services/result-http-request.service";

@Component({
  selector: 'app-result-table',
  templateUrl: './result-table.component.html',
  styleUrls: ['./result-table.component.css']
})
export class ResultTableComponent{
  @Input() results?: Result[]
  @Input() shipDto?: ShipDto[];
  @Input() questDto?: QuestDto[];

  constructor() {
    this.fetchResults()
  }

  fetchResults(){
  }

  mapIdToShip(id: string): string {
    if(this.shipDto===undefined) return "";
    return this.shipDto.find(ship => ship.id === id)?.name as string;
  }

  mapIdToQuest(id: string): string {
    if(this.questDto===undefined) return "";
    return this.questDto.find(quest => quest.id === id)?.name as string;
  }

}
