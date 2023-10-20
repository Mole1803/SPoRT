import { Component } from '@angular/core';
import {QuestPrototypeDto} from "../../models/quest-prototype-dto";
import {QuestManagerComponent} from "../quest-manager/quest-manager.component";
import {EditModalService} from "../../services/edit-modal.service";

@Component({
  selector: 'app-quest-table',
  templateUrl: './quest-table.component.html',
  styleUrls: ['./quest-table.component.css']
})
export class QuestTableComponent extends QuestManagerComponent{
  isActiveDropdownOpen = false;

  constructor(public override editModalService: EditModalService) {
    super(editModalService);

  }



  protected readonly Array = Array;
}
