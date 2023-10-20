import {Component, EventEmitter, Input, Output} from '@angular/core';
import {ShipDto} from "../../models/ship-dto";
import {AlertHandlerService} from "../../services/alert-handler.service";
import {AlertLevel} from "../../enums/alert-level";
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

  setCapacity(capacity: number) {
    // @ts-ignore
    this.editModalService.model.capacity = capacity;
  }

  getCapacity() {
    // @ts-ignore
    return this.editModalService.model.capacity;
  }

  setIsActive(isActive: boolean) {
    // @ts-ignore
    this.editModalService.model.isActive = isActive;
  }

  getIsActive() {
    // @ts-ignore
    return this.editModalService.model.isActive;
  }

  protected readonly ModalMode = ModalMode;
}
