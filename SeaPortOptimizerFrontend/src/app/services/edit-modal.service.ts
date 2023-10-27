import {EventEmitter, Injectable} from '@angular/core';
import {ModelBaseDto} from "../models/model-base-dto";
import {AlertHandlerService} from "./alert-handler.service";
import {AlertLevel} from "../enums/alert-level";
import {ModalMode} from "../enums/modal-mode";

@Injectable({
  providedIn: 'root'
})
export class EditModalService {
  isVisible: boolean = false;
  model?: ModelBaseDto;
  mode = ModalMode.EDIT;



  confirmationEmitter: EventEmitter<ModelBaseDto | undefined> = new EventEmitter<ModelBaseDto | undefined>();
  constructor(private alertHandlerService: AlertHandlerService) { }

  _open(model: ModelBaseDto) {
    this.isVisible = true;
    this.model = model;
  }

  close() {
    this.showAbortAlert()
    //this.confirmationEmitter.emit(undefined);
    this.reset()
  }

  confirm() {
    this.showAlert()
    this.confirmationEmitter.emit(this.model);
    this.reset()
  }

  changeModel(model: ModelBaseDto){
    this.model=model
    this.mode = ModalMode.EDIT
    this.showAlert()
    this.confirmationEmitter.emit(model)
    this.reset()
  }

  showAlert(){
    if(this.mode !== ModalMode.DELETE) this.alertHandlerService.showAlertWithAttributes('Success', `${this.model?.name} has been deleted.`, AlertLevel.SUCCESS);
    if(this.mode === ModalMode.EDIT) this.alertHandlerService.showAlertWithAttributes('Success', `${this.model?.name} has been edited.`, AlertLevel.SUCCESS);
    if(this.mode === ModalMode.ADD) this.alertHandlerService.showAlertWithAttributes('Success', `${this.model?.name} has been added.`, AlertLevel.SUCCESS);
  }

  showAbortAlert(){
      this.alertHandlerService.showAlertWithAttributes('Information', `No changes are made.`, AlertLevel.INFO);
  }

  isSafari(){
    if(navigator.userAgent.includes("Chrome")){
      return false;
    }
    return navigator.userAgent.includes('Safari');
  }

  reset() {
    this.model = undefined;
    this.mode = ModalMode.EDIT;
    this.isVisible = false
  }
}
