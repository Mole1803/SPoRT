import {Component} from '@angular/core';
import {QuestPrototypeDto} from "../../models/quest-prototype-dto";
import {QuestDto} from "../../models/quest-dto";
import {EditModalService} from "../../services/edit-modal.service";
import {ModalMode} from "../../enums/modal-mode";
import {QuestHttpRequestService} from "../../services/quest-http-request.service";

@Component({
  selector: 'app-quest-manager',
  templateUrl: './quest-manager.component.html',
  styleUrls: ['./quest-manager.component.css']
})
export class QuestManagerComponent {
  newQuestPrototype: QuestPrototypeDto = new QuestPrototypeDto("", true, "", 1, 0)
  quests: QuestDto[] = [];

  constructor(public editModalService: EditModalService, public questHttpRequestService: QuestHttpRequestService) {
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
    this.fetchQuests()
  }

  fetchQuests(){
    this.questHttpRequestService.list().subscribe((params => {
      this.quests = params
    }))
  }


  async addNewQuest(questPrototypeDto: QuestPrototypeDto) {
    let questDto = QuestDto.fromQuestPrototypeDto(questPrototypeDto);
    // validate questDto
    if (questDto.name === '' || questDto.demand < 0) return;
    let result = await this.questHttpRequestService.addQuest(questDto)
    result.subscribe()
    this.quests.unshift(questDto);
  }

  openAddQuestModal() {
    this.editModalService.mode = ModalMode.ADD;
    this.editModalService._open(new QuestPrototypeDto("", true, "", 1, 0));
  }


  deleteQuest(quest: QuestDto) {
    this.questHttpRequestService.deleteQuest(quest).subscribe()
    this.quests = this.quests.filter(s => s.name !== quest.name);
  }

  async editQuest(quest: QuestDto) {
    let result = await this.questHttpRequestService.updateQuest(quest)
    result.subscribe()
    this.quests = this.quests.map(q =>  q.id === quest.id ? quest : q);
  }
}
