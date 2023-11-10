import {Component, Output, Input, HostBinding, EventEmitter, IterableDiffers, DoCheck} from '@angular/core';
import {Tab} from "../../models/tab";
import {AppRoutes} from "../../enums/app-routes";
import {Router, Routes} from "@angular/router";


@Component({
  selector: 'app-nav-bar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.css']
})
export class NavBarComponent{

  // Routing tabs
  @Input() tabs: Tab[] = []
  @Output() tabChanged = new EventEmitter<Tab>();
  logoutHovered: boolean = false;

  setLogoutHovered(b:boolean){
    this.logoutHovered=b
  }

  logout(){
    localStorage.removeItem("token")
    this.router.navigate(['/'+AppRoutes.LOGIN])

  }

  // Indicator to show/hide the mobile menu
  isMobileMenuOpen: boolean = false;

  // Indicator to prevent unnatural fast opening/closing of the mobile menu
  blockTrigger: boolean = false;

  constructor(public router: Router){
  }


  /**
   * Sets the active tab.
   * @param tab
   */
  setActiveTab(tab: Tab) {
    this.tabChanged.emit(tab);
  }

  /**
   * Toggles the mobile menu.
   * Prevents fast opening/closing of the mobile menu. (100ms)
   */
  toggleSmallMenu() {
    if(this.blockTrigger) return;
    this.blockTrigger = true;
    this.isMobileMenuOpen = !this.isMobileMenuOpen;

    setTimeout(() => this.blockTrigger = false, 100);
  }

}
