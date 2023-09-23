import {Component, EventEmitter, HostBinding, Input, Output} from '@angular/core';

@Component({
  selector: 'app-delete-confirmation-modal',
  templateUrl: './delete-confirmation-modal.component.html',
  styleUrls: ['./delete-confirmation-modal.component.css']
})
export class DeleteConfirmationModalComponent {
  @Input() itemName: string | undefined = 'MyShip';
  @Input() isModalOpen: boolean = true;


  @Output() emitDeleteConfirmation = new EventEmitter<boolean>();

  constructor() {

  }

  onConfirmDelete() {
    this.emitDeleteConfirmation.emit(true);
    this.closeModal();
  }

  cancelDelete() {
    this.emitDeleteConfirmation.emit(false);
    this.closeModal();
  }


  closeModal() {
    this.isModalOpen = false;
  }

  protected readonly close = close;
}
