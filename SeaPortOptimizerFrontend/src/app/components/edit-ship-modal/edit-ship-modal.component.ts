import {Component} from '@angular/core';
import {EditModalService} from "../../services/edit-modal.service";
import {ModalMode} from "../../enums/modal-mode";

@Component({
  selector: 'app-edit-ship-modal',
  templateUrl: './edit-ship-modal.component.html',
  styleUrls: ['./edit-ship-modal.component.css']
})
export class EditShipModalComponent {
  //shipDto: ShipDto = new ShipDto('', '', -1, false);

  constructor(public editModalService: EditModalService) {

  }

  getName(){
    return this.editModalService.model?.name
  }

  setName(name: string){
    this.editModalService.model!.name=name
    this.checkAll()
  }

  setCapacity(capacity: number) {
    // @ts-ignore
    this.editModalService.model.capacity = capacity;
    this.checkAll()
  }

  getCapacity() {
    // @ts-ignore
    return this.editModalService.model.capacity;
  }

  setIsActive(isActive: boolean) {
    // @ts-ignore
    this.editModalService.model.is_active = isActive;
  }

  getIsActive() {
    // @ts-ignore
    return this.editModalService.model.is_active;
  }

  checkAll(){
    let confirm=document.getElementById("confirm")!
    if(typeof this.getName()=="string" && this.getName()!="" && this.getCapacity()>0){
      if (confirm.hasAttribute("disabled")) {
        confirm.removeAttribute("disabled")
      }
    }
    else if(!confirm.hasAttribute("disabled")) {
      confirm.setAttribute("disabled","disabled")
    }
  }

  protected readonly ModalMode = ModalMode;
}
