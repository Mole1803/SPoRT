import {EventEmitter, Injectable} from '@angular/core';
import {AlertLevel} from "../enums/alert-level";

@Injectable({
    providedIn: 'root'
})
export class AlertHandlerService {
    alertEmitter = new EventEmitter<boolean>();

    title: string = 'Our privacy policy has changed';
    message: string = 'Make sure you know how these changes affect you.'
    alertLevel: AlertLevel = AlertLevel.WARNING;

    constructor() {
    }

    setAlert(title: string, message: string, alertLevel: AlertLevel) {
        this.title = title;
        this.message = message;
        this.alertLevel = alertLevel;
    }

    showAlertWithAttributes(title: string, message: string, alertLevel: AlertLevel) {
        this.title = title;
        this.message = message;
        this.alertLevel = alertLevel;
        this.showAlert();
    }

    showAlert() {
        this.alertEmitter.emit(true);
    }
}
