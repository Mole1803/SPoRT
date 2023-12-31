import {Component, EventEmitter, HostBinding, Input, Output} from '@angular/core';
import {AlertHandlerService} from "../../services/alert-handler.service";
import {AlertLevel} from "../../enums/alert-level";
import {EditModalService} from "../../services/edit-modal.service";
import {ModalMode} from "../../enums/modal-mode";

@Component({
  selector: 'app-delete-confirmation-modal',
  templateUrl: './delete-confirmation-modal.component.html',
  styleUrls: ['./delete-confirmation-modal.component.css']
})
export class DeleteConfirmationModalComponent {
  @Input() itemName: string | undefined = 'MyShip';
  @Input() isModalOpen: boolean = true;


  @Output() emitDeleteConfirmation = new EventEmitter<boolean>();

  constructor(private alertHandlerService: AlertHandlerService, public editModalService: EditModalService) {

  }

  confirmDelete() {
    //this.emitDeleteConfirmation.emit(true);
    this.editModalService.confirm();
    //this.closeModal();
    //this.alertHandlerService.showAlertWithAttributes('Success', `${this.itemName} has been deleted.`, AlertLevel.SUCCESS);
  }

  cancelDelete() {
    this.editModalService.close();
    //this.emitDeleteConfirmation.emit(false);
    //this.closeModal();
  }


  closeModal() {
    this.isModalOpen = false;
  }

  protected readonly close = close;
  protected readonly ModalMode = ModalMode;
}
