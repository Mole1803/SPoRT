import {Component, Input} from '@angular/core';
import {QuestDto} from "../../models/quest-dto";

@Component({
  selector: 'app-quest-grid-element',
  templateUrl: './quest-grid-element.component.html',
  styleUrls: ['./quest-grid-element.component.css']
})
export class QuestGridElementComponent {
  @Input() questDto?: QuestDto;
}
