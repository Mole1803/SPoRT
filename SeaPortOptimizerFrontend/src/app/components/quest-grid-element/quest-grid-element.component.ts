import {Component, Input} from '@angular/core';
import {QuestDto} from "../../models/quest-dto";
import {EditModalService} from "../../services/edit-modal.service";

@Component({
  selector: 'app-quest-grid-element',
  templateUrl: './quest-grid-element.component.html',
  styleUrls: ['./quest-grid-element.component.css']
})
export class QuestGridElementComponent {
  @Input() questDto?: QuestDto;

  constructor(public editModalService: EditModalService) {
    editModalService.confirmationEmitter.subscribe((model) => {
      // @ts-ignore
      if (model.id === this.questDto?.id) {
        // @ts-ignore
        this.questDto = model;
      }
    })
  }

  createCopy() {
    return Object.assign({}, this.questDto);
  }
}
