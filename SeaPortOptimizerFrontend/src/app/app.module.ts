import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {HTTP_INTERCEPTORS, HttpClientModule} from "@angular/common/http";
import {environment} from "../environments/environment";
import { HomeComponent } from './views/home/home.component';
import { NavBarComponent } from './components/nav-bar/nav-bar.component';
import { HarborComponentComponent } from './components/harbor-component/harbor-component.component';
import { FleetViewComponent } from './views/fleet-view/fleet-view.component';
import { QuestViewComponent } from './views/quest-view/quest-view.component';
import { ShipTableComponent } from './components/ship-table/ship-table.component';
import { FooterComponent } from './components/footer/footer.component';
import {FormsModule} from "@angular/forms";
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ShipManagerComponent } from './components/ship-manager/ship-manager.component';
import { DeleteConfirmationModalComponent } from './components/delete-confirmation-modal/delete-confirmation-modal.component';
import { AlertComponent } from './components/alert/alert.component'
import {AlertHandlerService} from "./services/alert-handler.service";
import { EditShipModalComponent } from './components/edit-ship-modal/edit-ship-modal.component';
import { QuestTableComponent } from './components/quest-table/quest-table.component';
import { QuestManagerComponent } from './components/quest-manager/quest-manager.component';
import { QuestGridElementComponent } from './components/quest-grid-element/quest-grid-element.component';
import { EditQuestModalComponent } from './components/edit-quest-modal/edit-quest-modal.component';
import {EditModalService} from "./services/edit-modal.service";
import { ResultTableComponent } from './components/home/result-table/result-table.component';
import { RadioGroupComponent } from './components/home/radio-group/radio-group.component';
import { LoginComponent } from './views/login/login.component';
import {Auth} from "./auth/auth";


@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    NavBarComponent,
    HarborComponentComponent,
    FleetViewComponent,
    QuestViewComponent,
    ShipTableComponent,
    FooterComponent,
    ShipManagerComponent,
    DeleteConfirmationModalComponent,
    AlertComponent,
    EditShipModalComponent,
    QuestTableComponent,
    QuestManagerComponent,
    QuestGridElementComponent,
    EditQuestModalComponent,
    ResultTableComponent,
    RadioGroupComponent,
    LoginComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    BrowserAnimationsModule
  ],
  providers: [
    {provide: 'BASE_URL', useValue: environment.BASE_URL},
      AlertHandlerService,
    EditModalService,
    {
      provide: HTTP_INTERCEPTORS, useClass: Auth, multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
}
