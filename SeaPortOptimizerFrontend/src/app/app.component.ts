import {Component} from '@angular/core';
import {HttpUtilsService} from "./services/http-utils.service";
import {Tab} from "./models/tab";
import {AppRoutes} from "./enums/app-routes";
import {Router} from "@angular/router";
import {AlertHandlerService} from "./services/alert-handler.service";
import {AlertLevel} from "./enums/alert-level";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'SeaPortOptimizerFrontend';

  tabs: Tab[] = [
    new Tab('Home', AppRoutes.HOME, false),
    new Tab('Fleet', AppRoutes.FLEET, false),
    new Tab('Quest', AppRoutes.QUEST, false),
  ];

  constructor(private httpUtilsService: HttpUtilsService, private router: Router,private alertHandlerService: AlertHandlerService) {
    // Example of service usage
    httpUtilsService.isBackendAlive().subscribe((data) => {
       console.log(data)
      }, (error) => {
        this.alertHandlerService.showAlertWithAttributes("Error","Backend is not reachable!", AlertLevel.ERROR);
      }
    );

    if(!this.jwtTokenSet()){
      this.redirectToLogin();
    }
    // Routing
    this.setActiveRoute(this.sanitizeRoute(location.hash));


    this.httpUtilsService.jwtTokenTest().subscribe(
        (data) => {
          console.log(data)
        }
      )


  }

  sanitizeRoute(route: string | undefined) {
    if (route === undefined) {
      return ""
    }

    if(route.startsWith("#")) {
      route = route.substring(1);
    }

    if(route.startsWith("/")) {
      route = route.substring(1);
    }

    return route;
  }


  setActiveRoute(route: string) {
    if (route === undefined) {
      return
    }
    this.sanitizeRoute(route)

    this.tabs.forEach(t => t.active = false);
    let activeTab;
    for(let tab of this.tabs) {
      if (tab.route === route) {
        activeTab = tab;
        break;
      }
    }
    if (activeTab===undefined) {
      return
    }

    activeTab.active = true;
    this.title = activeTab.name;
  }

  redirectTo(tab: Tab) {
    this.router.navigate([tab.route]).then(() => this.setActiveRoute(this.sanitizeRoute(this.router.url)));
  }

  jwtTokenSet(){
    return localStorage.getItem("token") != null;
  }

  redirectToLogin(){
    this.router.navigate([AppRoutes.LOGIN]).then(() => this.setActiveRoute(this.sanitizeRoute(this.router.url)));
  }

  isFooterAndHeaderHidden(){
    return this.router.url !== "/"+AppRoutes.LOGIN;
  }


}
