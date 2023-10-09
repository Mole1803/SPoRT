import {Component, Input} from '@angular/core';
import {AlertLevel} from "../../enums/alert-level";
import {GuidGenerator} from "../../utilities/guid-generator";
import {AlertHandlerService} from "../../services/alert-handler.service";
import {animate, style, transition, trigger} from "@angular/animations";

@Component({
  selector: 'app-alert',
  templateUrl: './alert.component.html',
  styleUrls: ['./alert.component.css'],
  animations: [
  trigger('fadeInOut', [
    transition(':enter', [
      style({opacity:0}),
      animate(150, style({opacity:1}))
    ]),
    transition(':leave', [
      animate(125, style({opacity:0}))
    ])
  ])
  ]
})
export class AlertComponent {
  isAlertVisible: boolean = false;
  title: string = 'Our privacy policy has changed';
  message: string = 'Make sure you know how these changes affect you.'
  alertLevel: AlertLevel = AlertLevel.WARNING;

  id: string = ""

  constructor(private alertHandlerService: AlertHandlerService) {
    alertHandlerService.alertEmitter.subscribe(() => {
      this.initializeAlertFromAlertHandlerService()
      this.open()
    });

  }


  close() {
    this.isAlertVisible = false;
  }

  open() {
    this.isAlertVisible = true;
    let localId = GuidGenerator.newGuidV4();
    this.id = localId;

    setTimeout(() => {
      if(this.id !== localId) return;
      this.close()
    }, 5000);
  }

  private initializeAlertFromAlertHandlerService(){
    this.title = this.alertHandlerService.title
    this.message = this.alertHandlerService.message
    this.alertLevel = this.alertHandlerService.alertLevel
  }

  protected readonly AlertLevel = AlertLevel;
}
