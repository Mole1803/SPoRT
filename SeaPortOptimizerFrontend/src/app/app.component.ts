import { Component } from '@angular/core';
import {HttpUtilsService} from "./services/http-utils.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'SeaPortOptimizerFrontend';
  constructor(private httpUtilsService: HttpUtilsService) {
    httpUtilsService.isBackendAlive().subscribe((data) => {
      console.log(data);

    }
    );
  }
}
