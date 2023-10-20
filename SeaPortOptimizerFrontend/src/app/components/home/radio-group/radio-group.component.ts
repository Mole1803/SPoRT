import { Component } from '@angular/core';
import {Algorithm} from "../../../enums/algorithm";

@Component({
  selector: 'app-radio-group',
  templateUrl: './radio-group.component.html',
  styleUrls: ['./radio-group.component.css']
})
export class RadioGroupComponent {
  availableAlgorithms = [Algorithm.MARCEL, Algorithm.RUBEN , Algorithm.TIM, Algorithm.MORITZ ];

}
