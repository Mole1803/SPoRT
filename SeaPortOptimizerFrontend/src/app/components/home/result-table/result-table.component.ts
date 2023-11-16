import {Component, Input} from '@angular/core';
import {Result} from "../../../models/result";
import {ShipDto} from "../../../models/ship-dto";
import {QuestDto} from "../../../models/quest-dto";

@Component({
  selector: 'app-result-table',
  templateUrl: './result-table.component.html',
  styleUrls: ['./result-table.component.css']
})
export class ResultTableComponent{
  @Input() results?: Result[]
  @Input() shipDto?: ShipDto[];
  @Input() questDto?: QuestDto[];
  @Input() current: number=0;

  constructor() {
    this.fetchResults()
  }

  fetchResults(){
  }

  /*checkNextPage(){
    let next=document.getElementById("next")!
    let previous=document.getElementById("previous")!
    previous.removeAttribute("disabled")
    if(this.current>this.results!.length-2) {
      next.setAttribute("disabled", "disabled")
    }
  }

  checkPreviousPage(){
    let next=document.getElementById("next")!
    let previous=document.getElementById("previous")!
    next.removeAttribute("disabled")
    if(this.current<1) {
      previous.setAttribute("disabled", "disabled")
    }
  }*/
  hasNextPage(){
    return this.current<this.results!.length-1
  }
  hasPreviousPage(){
    return this.current>0
  }

  nextPage(){
    if(this.current<this.results!.length-1){
      this.current+=1
    }

  }
  previousPage(){
    if(this.current>0){
      this.current-=1
    }
  }

  getResult(i: number){

    // @ts-ignore
    return this.results[i]
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
