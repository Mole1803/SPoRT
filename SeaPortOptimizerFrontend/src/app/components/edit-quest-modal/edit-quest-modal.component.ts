import {Component} from '@angular/core';
import {EditModalService} from "../../services/edit-modal.service";
import {ModalMode} from "../../enums/modal-mode";

@Component({
  selector: 'app-edit-quest-modal',
  templateUrl: './edit-quest-modal.component.html',
  styleUrls: ['./edit-quest-modal.component.css']
})
export class EditQuestModalComponent {
  constructor(public editModalService: EditModalService) {
  }

  getName(){
    return this.editModalService.model?.name
  }

  setName(name: string){
    this.editModalService.model!.name=name
    this.checkAll()
  }

  getDemand(){
    // @ts-ignore
    if(this.editModalService.model.demand!=-1) {
      // @ts-ignore
      return this.editModalService.model.demand
    }
    return null
  }

  setDemand(demand: number){
    // @ts-ignore
    this.editModalService.model.demand = demand
    this.checkAll()
  }

  setIsActive(isActive: boolean){
    // @ts-ignore
    this.editModalService.model.isActive = isActive
    this.checkAll()
  }

  getIsActive(){
    // @ts-ignore
    return this.editModalService.model.isActive
  }

  setRessource(resource: string){
    // @ts-ignore
    this.editModalService.model.resource = resource
    this.checkAll()
  }

  getRessource() {
    // @ts-ignore
    return this.editModalService.model.resource
  }

  setItemsPerCapacity(multiplier: number){
    // @ts-ignore
    this.editModalService.model.itemsPerCapacity = multiplier
    this.checkAll()
  }

  getItemsPerCapacity() {
    // @ts-ignore
    if (this.editModalService.model.itemsPerCapacity!=-1){
      // @ts-ignore
      return this.editModalService.model.itemsPerCapacity
    }
    return null
  }

  checkAll(){
    let confirm=document.getElementById("confirm")!
    if(this.getDemand()>0 && this.getItemsPerCapacity()>0 && this.getRessource()!="" && this.editModalService.model?.name!=""){
      confirm.removeAttribute("disabled")
    }
    else if(!confirm.hasAttribute("disabled")) {
      confirm.setAttribute("disabled","disabled")
    }
  }


  protected readonly ModalMode = ModalMode;
  protected readonly EditModalService = EditModalService;
}
