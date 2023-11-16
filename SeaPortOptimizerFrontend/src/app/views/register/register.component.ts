import { Component } from '@angular/core';
import {HttpUtilsService} from "../../services/http-utils.service";
import {Router} from "@angular/router";
import {AppRoutes} from "../../enums/app-routes";
import {AlertHandlerService} from "../../services/alert-handler.service";
import {AlertLevel} from "../../enums/alert-level";

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  username : string = "";
  password : string = "";
  confirm_password : string = "";

  constructor(private httpUtilsService: HttpUtilsService, private router: Router, public alertHandlerService: AlertHandlerService) {

  }

  async register(username: string, password: string, confirm_password: string) {
    if(username == "" || password == "") return
    if(password !== confirm_password) return
    let result = await this.httpUtilsService.register(username, password);
    result.subscribe(jwt => {
      this.saveToken(jwt);
      this.redirectToHome()
    }
    , error => {
      this.alertHandlerService.showAlertWithAttributes(error.error.message, "", AlertLevel.ERROR);
    }
    );
    return


  }

  saveToken(jwt: any) {
    localStorage.setItem("token", jwt.access_token);
  }

  redirectToHome() {
    this.router.navigate([""+AppRoutes.HOME]);
  }
  redirectToLogin(){
    return "#/"+AppRoutes.LOGIN
  }

}
