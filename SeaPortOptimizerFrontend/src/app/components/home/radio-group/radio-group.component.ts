import {Component, EventEmitter, Input, Output} from '@angular/core';
import {Algorithm} from "../../../enums/algorithm";
import {Method} from "../../../enums/method";
import {ResultHttpRequestService} from "../../../services/result-http-request.service";
import {ResultTableComponent} from "../result-table/result-table.component";
import {Round} from "../../../models/round";
import {Result} from "../../../models/result";
import {Step} from "../../../models/step";
import {AlgorithmChoice} from "../../../models/algorithm-choice";


@Component({
  selector: 'app-radio-group',
  templateUrl: './radio-group.component.html',
  styleUrls: ['./radio-group.component.css']
})
export class RadioGroupComponent {
  metho?: Method = undefined
  algo?: Algorithm = undefined
  availableAlgorithms = [Algorithm.MARCEL, Algorithm.RUBEN, Algorithm.TIM, Algorithm.MORITZ];
  availableMethods = [Method.TIME, Method.RESOURCE]
  @Output() fetchDataEmitter: EventEmitter<AlgorithmChoice> = new EventEmitter<AlgorithmChoice>()

  constructor(public resultHttpRequestService: ResultHttpRequestService) {
    this.resultHttpRequestService = resultHttpRequestService

  }

  start() {
    console.log(this.algo,this.metho)
    if (this.algo === undefined || this.metho === undefined) {
      return
    }
    let x: AlgorithmChoice = new AlgorithmChoice(this.algo, this.metho)
    this.fetchDataEmitter.emit(x)
  }
}
