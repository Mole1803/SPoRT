import { Component } from '@angular/core';
import {HttpUtilsService} from "../../services/http-utils.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  constructor(private httpUtilsService: HttpUtilsService) {
    this.login()
  }

  async login(username: string = "admin", password: string = "admin") {
    let result = await this.httpUtilsService.login(username, password);
    result.subscribe(jwt => {
      this.saveToken(jwt);

    }
    );


  }

  saveToken(jwt: any) {
    localStorage.setItem("token", jwt.access_token);
  }

}
