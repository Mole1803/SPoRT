import {Component, EventEmitter, Input, Output} from '@angular/core';
import {ShipDto} from "../../models/ship-dto";
import {AlertHandlerService} from "../../services/alert-handler.service";
import {AlertLevel} from "../../enums/alert-level";

@Component({
  selector: 'app-edit-ship-modal',
  templateUrl: './edit-ship-modal.component.html',
  styleUrls: ['./edit-ship-modal.component.css']
})
export class EditShipModalComponent {
  @Input() @Output() isVisible: boolean = true;
  @Input() shipDto: ShipDto = new ShipDto('', '', -1, false);

  @Output() confirmationEmitter: EventEmitter<ShipDto | undefined> = new EventEmitter<ShipDto | undefined>();

  constructor(private alertHandlerService: AlertHandlerService) {
  }


  close() {
    this.alertHandlerService.showAlertWithAttributes('Information', `No changes are made.`, AlertLevel.INFO);
    this.confirmationEmitter.emit(undefined);
    this._close()
  }
  _close() {
    this.isVisible = false;
  }

  confirm() {
    this.confirmationEmitter.emit(this.shipDto);
    this.alertHandlerService.showAlertWithAttributes('Success', `${this.shipDto.name} has been edited.`, AlertLevel.SUCCESS);
    this._close()
  }

}
