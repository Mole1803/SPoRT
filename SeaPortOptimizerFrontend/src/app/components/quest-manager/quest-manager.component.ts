import { Component } from '@angular/core';
import {QuestPrototypeDto} from "../../models/quest-prototype-dto";
import {QuestDto} from "../../models/quest-dto";

@Component({
  selector: 'app-quest-manager',
  templateUrl: './quest-manager.component.html',
  styleUrls: ['./quest-manager.component.css']
})
export class QuestManagerComponent {
  newQuestPrototype: QuestPrototypeDto = new QuestPrototypeDto("", true,"",1,0)
  quests: QuestDto[] = [];

  constructor() {
    for(let i=0; i<100;i++){
      let questPrototype = new QuestPrototypeDto("Quest "+i, (i%2)==1,"Holz",1,100)
      this.quests.push(QuestDto.fromQuestPrototypeDto(questPrototype))
    }

  }

  addNewQuest() {
    if(this.newQuestPrototype.name === '' || this.newQuestPrototype.demand === 0) return;
    this.newQuestPrototype = new QuestPrototypeDto("", true,"",1,0)
  }

  markForEdit(quest: QuestDto) {
    this.newQuestPrototype = Object.assign({}, quest);
  }

  markForDeletion(quest: QuestDto) {
    this.quests = this.quests.filter(s => s.name !== quest.name);
  }
}
