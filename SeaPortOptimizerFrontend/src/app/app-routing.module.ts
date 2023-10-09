import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {HomeComponent} from "./views/home/home.component";
import {FleetViewComponent} from "./views/fleet-view/fleet-view.component";
import {AppRoutes} from "./enums/app-routes";
import {QuestViewComponent} from "./views/quest-view/quest-view.component";

const routes: Routes = [
  { path: AppRoutes.HOME,  component: HomeComponent},
  { path: AppRoutes.FLEET,  component: FleetViewComponent},
  { path: AppRoutes.QUEST,  component: QuestViewComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {useHash: true})],
  exports: [RouterModule]
})
export class AppRoutingModule { }
