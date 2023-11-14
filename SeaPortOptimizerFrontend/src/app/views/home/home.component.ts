import {Component, Input} from '@angular/core';
import {Result} from "../../models/result";
import {ResultHttpRequestService} from "../../services/result-http-request.service";
import {AlgorithmChoice} from "../../models/algorithm-choice";
import {ShipHttpRequestService} from "../../services/ship-http-request.service";
import {QuestHttpRequestService} from "../../services/quest-http-request.service";
import {ShipDto} from "../../models/ship-dto";
import {QuestDto} from "../../models/quest-dto";
import {forkJoin, Observable, switchMap} from "rxjs";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  @Input() results: Result[] = [];
  ships: ShipDto[] = [];
  quests: QuestDto[] = []

  constructor(public resultHttpRequestService: ResultHttpRequestService,
              public shipHttpRequestService: ShipHttpRequestService,
              public questHttpRequestService: QuestHttpRequestService) {
  }


  async getResult(algorithmChoice: AlgorithmChoice) {
    let sources: [Observable<QuestDto[]>, Observable<ShipDto[]>] = [this.questHttpRequestService.list(), this.shipHttpRequestService.list()]
    let result = await forkJoin(sources).pipe(switchMap((results: [QuestDto[], ShipDto[]]) => {
        this.quests = results[0]
        this.ships = results[1]
        return this.resultHttpRequestService.getResult(algorithmChoice.algorithm, algorithmChoice.method)
      }
    ))
    result.subscribe((params => {
      this.results = params
    }))
  }
}
