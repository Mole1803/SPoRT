import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {HttpClientModule} from "@angular/common/http";
import {environment} from "../environments/environment";
import { HomeComponent } from './views/home/home.component';
import { NavBarComponent } from './components/nav-bar/nav-bar.component';
import { HarborComponentComponent } from './components/harbor-component/harbor-component.component';
import { FleetViewComponent } from './views/fleet-view/fleet-view.component';
import { QuestViewComponent } from './views/quest-view/quest-view.component';


@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    NavBarComponent,
    HarborComponentComponent,
    FleetViewComponent,
    QuestViewComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [
    {provide: 'BASE_URL', useValue: environment.BASE_URL},
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
}
