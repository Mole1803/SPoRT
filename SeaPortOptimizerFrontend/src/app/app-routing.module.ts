import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {HomeComponent} from "./views/home/home.component";
import {FleetViewComponent} from "./views/fleet-view/fleet-view.component";
import {AppRoutes} from "./enums/app-routes";
import {QuestViewComponent} from "./views/quest-view/quest-view.component";
import {LoginComponent} from "./views/login/login.component";
import {authGuard} from "./auth/auth.guard";
import {RegisterComponent} from "./views/register/register.component";

const routes: Routes = [
  { path: AppRoutes.HOME,  component: HomeComponent, canActivate: [authGuard]},
  { path: AppRoutes.FLEET,  component: FleetViewComponent, canActivate: [authGuard]},
  { path: AppRoutes.QUEST,  component: QuestViewComponent, canActivate: [authGuard]},
  { path: AppRoutes.LOGIN,  component: LoginComponent},
  { path: AppRoutes.REGISTER,  component: RegisterComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {useHash: true})],
  exports: [RouterModule]
})
export class AppRoutingModule { }
