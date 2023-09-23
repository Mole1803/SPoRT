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
import { ShipTableComponent } from './components/ship-table/ship-table.component';
import { FooterComponent } from './components/footer/footer.component';
import {FormsModule} from "@angular/forms";
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ShipManagerComponent } from './components/ship-manager/ship-manager.component';
import { DeleteConfirmationModalComponent } from './components/delete-confirmation-modal/delete-confirmation-modal.component'


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
    DeleteConfirmationModalComponent
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
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
}
