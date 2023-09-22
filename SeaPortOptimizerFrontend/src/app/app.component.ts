import {Component, EventEmitter, ViewChild} from '@angular/core';
import {HttpUtilsService} from "./services/http-utils.service";
import {Tab} from "./models/tab";
import {AppRoutes} from "./enums/app-routes";
import {Router} from "@angular/router";
import {NavBarComponent} from "./components/nav-bar/nav-bar.component";

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

  constructor(private httpUtilsService: HttpUtilsService, private router: Router) {
    // Example of service usage
    httpUtilsService.isBackendAlive().subscribe((data) => {
        console.log(data);
      }
    );

    // Routing
    this.setActiveRoute(this.sanitizeRoute(location.hash));
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


}
