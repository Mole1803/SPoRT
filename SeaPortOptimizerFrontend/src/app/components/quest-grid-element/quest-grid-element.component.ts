import {Component, Input} from '@angular/core';
import {QuestDto} from "../../models/quest-dto";
import {EditModalService} from "../../services/edit-modal.service";
import {ModalMode} from "../../enums/modal-mode";

@Component({
  selector: 'app-quest-grid-element',
  templateUrl: './quest-grid-element.component.html',
  styleUrls: ['./quest-grid-element.component.css']
})
export class QuestGridElementComponent {
  @Input() questDto?: QuestDto;

  constructor(public editModalService: EditModalService) {
  }

  deleteQuest() {
    this.editModalService.mode = ModalMode.DELETE;
    // @ts-ignore
    this.editModalService._open(this.questDto);
  }

  editQuest() {
    this.editModalService.mode = ModalMode.EDIT;
    this.editModalService._open(this.createCopy());
  }

  createCopy() {
    return Object.assign({}, this.questDto);
  }
}
