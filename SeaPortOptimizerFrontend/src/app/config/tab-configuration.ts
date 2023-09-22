import {Tab} from "../models/tab";
import {AppRoutes} from "../enums/app-routes";

export class TabConfiguration {
    tabs: Tab[] = [
    new Tab('Home', AppRoutes.HOME, false),
    new Tab('Fleet', AppRoutes.FLEET, false),
    new Tab('Quest', AppRoutes.QUEST, false),
  ];
}
