import { Component } from '@angular/core';
import {HttpUtilsService} from "../../services/http-utils.service";
import {Router} from "@angular/router";
import {AppRoutes} from "../../enums/app-routes";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username : string = "";
  password : string = "";

  constructor(private httpUtilsService: HttpUtilsService, private router: Router) {

  }

  async login(username: string, password: string) {
    if(username == "" || password == "") return
    let result = await this.httpUtilsService.login(username, password);
    result.subscribe(jwt => {
      this.saveToken(jwt);
      this.redirectToHome()
    }
    );


  }

  saveToken(jwt: any) {
    localStorage.setItem("token", jwt.access_token);
  }

  redirectToHome() {
    this.router.navigate([AppRoutes.HOME]);
  }

}
