import {Component, HostListener, Input} from '@angular/core';

import {style, state, animate, transition, trigger} from '@angular/animations';

import {ShipManagerComponent} from "../ship-manager/ship-manager.component";
import {EditModalService} from "../../services/edit-modal.service";
import {ShipDto} from "../../models/ship-dto";

@Component({
  selector: 'app-ship-table',
  templateUrl: './ship-table.component.html',
  styleUrls: ['./ship-table.component.css'],
  animations: [
  trigger('fadeInOut', [
    transition(':enter', [
      style({opacity:0}),
      animate(150, style({opacity:1}))
    ]),
    transition(':leave', [
      animate(125, style({opacity:0}))
    ])
  ])
  ]
})
export class ShipTableComponent extends ShipManagerComponent{
  isActiveDropdownOpen: boolean = false;
  isLargeScreen: boolean = false;


  @HostListener('document:click', ['$event']) clickout(event: any) {
    if(event.target.id !== 'isActive-dropdown-button' && (event.target.role !== 'menuitem' && event.target.parentNode?.id !== 'isActive-dropdown-menu'))
    {
      this.isActiveDropdownOpen = false;
    }
  }


  @HostListener('window:resize', ['$event'])
  onResize(event: Event) {
    this.detectScreenSize();
  }




  constructor(public override editModalService: EditModalService) {
    super(editModalService);

  }


  detectScreenSize() {
    this.isLargeScreen = window.innerWidth >= 1024;
  }

  openEditModal(ship: ShipDto) {
    this.editModalService._open(ship);
  }



  protected readonly Object = Object;
}
