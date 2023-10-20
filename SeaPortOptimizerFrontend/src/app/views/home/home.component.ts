import {Component} from '@angular/core';
import {Result} from "../../models/result";
import {Step} from "../../models/step";
import {Round} from "../../models/round";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  result?: Result;

  constructor() {
    let round: Round[] = [];

    for(let j = 0; j < 10; j++) {
      let step: Step[] = [];
      for(let i = 0; i < 10; i++) {
        step.push(new Step("ship "+i.toString(),"quest "+ i.toString(), i));
      }
      round.push(new Round(step));
    }

    this.result = new Result(round);
    console.log(this.result)
  }
}
