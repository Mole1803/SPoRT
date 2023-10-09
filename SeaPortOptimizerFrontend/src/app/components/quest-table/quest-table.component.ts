import { Component } from '@angular/core';
import {QuestPrototypeDto} from "../../models/quest-prototype-dto";
import {QuestManagerComponent} from "../quest-manager/quest-manager.component";

@Component({
  selector: 'app-quest-table',
  templateUrl: './quest-table.component.html',
  styleUrls: ['./quest-table.component.css']
})
export class QuestTableComponent extends QuestManagerComponent{
  isActiveDropdownOpen = false;


  protected readonly Array = Array;
}
