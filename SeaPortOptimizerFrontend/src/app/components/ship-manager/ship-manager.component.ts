import {Component, Input} from '@angular/core';
import {ShipDto} from "../../models/ship-dto";
import {ShipPrototypeDto} from "../../models/ship-prototype-dto";
import {GuidGenerator} from "../../utilities/guid-generator";

@Component({
  selector: 'app-ship-manager',
  templateUrl: './ship-manager.component.html',
  styleUrls: ['./ship-manager.component.css']
})
export class ShipManagerComponent {
  @Input() ships: ShipDto[] = [];
  newShipPrototype: ShipPrototypeDto = new ShipPrototypeDto('', 0, true);
  selectedItem: ShipDto | undefined = undefined;

  isDeleteWindowOpen: boolean = false;
  isEditWindowOpen: boolean = false;

  constructor() {
    for (let x = 0; x < 100; x++) {
      this.ships.push(new ShipDto(GuidGenerator.newGuidV4(), `Ship ${x}`, 100, true));
    }
  }

  addNewShip() {
    if(this.newShipPrototype.name === '' || this.newShipPrototype.capacity === 0) return;
    this.ships.splice(0, 0, ShipDto.fromShipPrototypeDto(this.newShipPrototype));
    this.newShipPrototype = new ShipPrototypeDto('', 0, true);
  }

  markForDeletion(ship: ShipDto) {
    this.selectedItem = ship;
    this.isDeleteWindowOpen = true;
  }

  deleteShip(isDeleteConfirmed: boolean) {
    this.isDeleteWindowOpen = false;
    if (!isDeleteConfirmed) return;
    this.ships = this.ships.filter(s => s.id !== this.selectedItem?.id);

  }

  markForEdit(ship: ShipDto) {
    this.selectedItem = ship;
    this.isEditWindowOpen = true;
  }

  editShip(ship: ShipDto | undefined) {
    this.isEditWindowOpen = false;
    if (ship === undefined) return;
    this.ships = this.ships.map(s => s.id === ship.id ? ship : s);
  }

}
