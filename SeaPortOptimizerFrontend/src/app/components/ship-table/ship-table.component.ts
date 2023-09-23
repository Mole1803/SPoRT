import {Component, HostListener, Input} from '@angular/core';
import {ShipDto} from "../../models/ship-dto";
import {ShipPrototypeDto} from "../../models/ship-prototype-dto";
import {GuidGenerator} from "../../utilities/guid-generator";

import {style, state, animate, transition, trigger} from '@angular/animations';

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
export class ShipTableComponent {

  @Input() ships: ShipDto[] = [];

  newShipPrototype: ShipPrototypeDto = new ShipPrototypeDto('', 0, true);

  isActiveDropdownOpen: boolean = false;
  isLargeScreen: boolean = false;

  @HostListener('document:click', ['$event']) clickout(event: any) {
    console.log(event.target.id, event.target.role, event.target.parentNode)
    if(event.target.id !== 'isActive-dropdown-button' && (event.target.role !== 'menuitem' && event.target.parentNode?.id !== 'isActive-dropdown-menu'))
    {
      this.isActiveDropdownOpen = false;
    }
  }

  @HostListener('window:resize', ['$event'])
  onResize(event: Event) {
    this.detectScreenSize();
  }


  constructor() {
    for(let x=0; x<100; x++){
      this.ships.push(new ShipDto(GuidGenerator.newGuidV4(), `Ship ${x}`, 100, true));
    }
    console.log(GuidGenerator.newGuidV4())
  }

  addNewShip() {
    this.ships.splice(0,0,ShipDto.fromShipPrototypeDto(this.newShipPrototype));
    this.newShipPrototype = new ShipPrototypeDto('', 0, true);
  }

  detectScreenSize() {
    this.isLargeScreen = window.innerWidth >= 1024;
  }


}
