import {Component} from '@angular/core';
import {QuestPrototypeDto} from "../../models/quest-prototype-dto";
import {QuestDto} from "../../models/quest-dto";
import {EditModalService} from "../../services/edit-modal.service";
import {ModalMode} from "../../enums/modal-mode";

@Component({
  selector: 'app-quest-manager',
  templateUrl: './quest-manager.component.html',
  styleUrls: ['./quest-manager.component.css']
})
export class QuestManagerComponent {
  newQuestPrototype: QuestPrototypeDto = new QuestPrototypeDto("", true, "", 1, 0)
  quests: QuestDto[] = [];

  constructor(public editModalService: EditModalService) {
    editModalService.confirmationEmitter.subscribe((model) => {
        if (this.editModalService.mode === ModalMode.ADD) {
          let questPrototypeDto = model as QuestPrototypeDto;
          this.addNewQuest(questPrototypeDto);
        }
        if (this.editModalService.mode === ModalMode.DELETE) {
          let questDto = model as QuestDto;
          this.deleteQuest(questDto);
        }
        if (this.editModalService.mode === ModalMode.EDIT) {
          let questDto = model as QuestDto;
          this.editQuest(questDto);
        }

      }
    )

    for (let i = 0; i < 100; i++) {
      let questPrototype = new QuestPrototypeDto("Quest " + i, (i % 2) == 1, "Holz", 1, 100)
      this.quests.push(QuestDto.fromQuestPrototypeDto(questPrototype))
    }

  }

  addNewQuest(questPrototypeDto: QuestPrototypeDto) {
    let questDto = QuestDto.fromQuestPrototypeDto(questPrototypeDto);
    // validate questDto
    if (questDto.name === '' || questDto.demand < 0) return;
    // Todo: Save to backend

    this.quests.unshift(questDto);
  }

  openAddQuestModal() {
    this.editModalService.mode = ModalMode.ADD;
    this.editModalService._open(new QuestPrototypeDto("", true, "", 1, 0));
  }


  deleteQuest(quest: QuestDto) {
    // Todo: Save to backend
    this.quests = this.quests.filter(s => s.name !== quest.name);
  }

  editQuest(quest: QuestDto) {
    this.quests = this.quests.map(q =>  q.id === quest.id ? quest : q);
  }
}
