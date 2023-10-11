import {Component, EventEmitter, Input, Output} from '@angular/core';
import {AlertLevel} from "../../enums/alert-level";
import {ShipDto} from "../../models/ship-dto";
import {AlertHandlerService} from "../../services/alert-handler.service";
import {QuestDto} from "../../models/quest-dto";
import {EditModalService} from "../../services/edit-modal.service";

@Component({
  selector: 'app-edit-quest-modal',
  templateUrl: './edit-quest-modal.component.html',
  styleUrls: ['./edit-quest-modal.component.css']
})
export class EditQuestModalComponent {
  constructor(public editModalService: EditModalService) {
  }

  getDemand(){
    // @ts-ignore
    return this.editModalService.model.demand
  }

  setDemand(demand: number){
    // @ts-ignore
    this.editModalService.model.demand = demand
  }

  setIsActive(isActive: boolean){
    // @ts-ignore
    this.editModalService.model.isActive = isActive
  }

  getIsActive(){
    // @ts-ignore
    return this.editModalService.model.isActive
  }

  setRessource(resource: string){
    // @ts-ignore
    this.editModalService.model.resource = resource
  }

  getRessource() {
    // @ts-ignore
    return this.editModalService.model.resource
  }

  setItemsPerCapacity(multiplier: number){
    // @ts-ignore
    this.editModalService.model.itemsPerCapacity = multiplier
  }

  getItemsPerCapacity() {
    // @ts-ignore
    return this.editModalService.model.itemsPerCapacity
  }


}
