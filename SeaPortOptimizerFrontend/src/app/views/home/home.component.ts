import {Component, Input} from '@angular/core';
import {Result} from "../../models/result";
import {ResultHttpRequestService} from "../../services/result-http-request.service";
import {AlgorithmChoice} from "../../models/algorithm-choice";
import {ShipHttpRequestService} from "../../services/ship-http-request.service";
import {QuestHttpRequestService} from "../../services/quest-http-request.service";
import {ShipDto} from "../../models/ship-dto";
import {QuestDto} from "../../models/quest-dto";
import {forkJoin, Observable, switchMap} from "rxjs";
import {AlertHandlerService} from "../../services/alert-handler.service";
import {AlertLevel} from "../../enums/alert-level";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  @Input() results?: Result[];
  ships: ShipDto[] = [];
  quests: QuestDto[] = []
  pageNumber: number = 0;

  constructor(public resultHttpRequestService: ResultHttpRequestService,
              public shipHttpRequestService: ShipHttpRequestService,
              public questHttpRequestService: QuestHttpRequestService,
              public alertHandlerService:AlertHandlerService) {
  }


  async getResult(algorithmChoice: AlgorithmChoice) {
    let sources: [Observable<QuestDto[]>, Observable<ShipDto[]>] = [this.questHttpRequestService.list(), this.shipHttpRequestService.list()]
    let result = await forkJoin(sources).pipe(switchMap((results: [QuestDto[], ShipDto[]]) => {
        this.quests = results[0]
        this.ships = results[1]
        //verify at least one ship is set to true
        let shipSet = false
        for (let ship of this.ships) {
          if (ship.is_active) {
            shipSet = true
            break
          }
        }
        if(!shipSet){
          this.alertHandlerService.showAlertWithAttributes("No ship selected","Please select at least one ship",AlertLevel.ERROR)
          return new Observable<Result[]>()
        }

        return this.resultHttpRequestService.getResult(algorithmChoice.algorithm, algorithmChoice.method)
      }
    )
      )
    result.subscribe((params => {
      this.pageNumber = 0
      this.results = params
    }),error => {
      if(error.status == 400) {
        this.alertHandlerService.showAlertWithAttributes("Error", "Quest list can't be empty.", AlertLevel.ERROR)
      }
    })
  }
}
