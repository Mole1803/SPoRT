import {EventEmitter, Injectable} from '@angular/core';
import {ModelBaseDto} from "../models/model-base-dto";
import {AlertHandlerService} from "./alert-handler.service";
import {AlertLevel} from "../enums/alert-level";

@Injectable({
  providedIn: 'root'
})
export class EditModalService {
  isVisible: boolean = false;
  model?: ModelBaseDto;

  confirmationEmitter: EventEmitter<ModelBaseDto | undefined> = new EventEmitter<ModelBaseDto | undefined>();
  constructor(private alertHandlerService: AlertHandlerService) { }

  _open(model: ModelBaseDto) {
    console.log("open")
    this.isVisible = true;
    this.model = model;
  }

  _close() {
    this.isVisible = false;
  }

  close() {
    this.alertHandlerService.showAlertWithAttributes('Information', `No changes are made.`, AlertLevel.INFO);
    this.confirmationEmitter.emit(undefined);
    this._close()
  }

  confirm() {
    this.alertHandlerService.showAlertWithAttributes('Success', `${this.model?.name} has been edited.`, AlertLevel.SUCCESS);
    this.confirmationEmitter.emit(this.model);
    this._close()
  }

  isSafari(){
    if(navigator.userAgent.includes("Chrome")){
      return false;
    }
    return navigator.userAgent.includes('Safari');
  }
}
