import {Component, Input} from '@angular/core';
import {ShipDto} from "../../models/ship-dto";
import {ShipPrototypeDto} from "../../models/ship-prototype-dto";
import {GuidGenerator} from "../../utilities/guid-generator";
import {EditModalService} from "../../services/edit-modal.service";
import {ModalMode} from "../../enums/modal-mode";

@Component({
  selector: 'app-ship-manager',
  templateUrl: './ship-manager.component.html',
  styleUrls: ['./ship-manager.component.css']
})
export class ShipManagerComponent {
  @Input() ships: ShipDto[] = [];
  newShipPrototype: ShipPrototypeDto = new ShipPrototypeDto('', 0, true);



  constructor(public editModalService: EditModalService) {
    this.editModalService.reset();

    editModalService.confirmationEmitter.subscribe((ship: ShipDto | undefined ) => {
      if(ship === undefined) return;
      if(editModalService.mode === ModalMode.EDIT) this.editShip(ship);
      if(editModalService.mode === ModalMode.DELETE) this.deleteShip(ship);

    }

    )

    for (let x = 0; x < 100; x++) {
      this.ships.push(new ShipDto(GuidGenerator.newGuidV4(), `Ship ${x}`, 100, true));
    }
  }


  openEditModal(ship: ShipDto) {
    this.editModalService.mode = ModalMode.EDIT;
    this.editModalService._open(Object.assign({}, ship));
  }

  openDeleteModal(ship: ShipDto) {
    this.editModalService.mode = ModalMode.DELETE;
    this.editModalService._open(ship);
  }

  addNewShip() {
    if(this.newShipPrototype.name === '' || this.newShipPrototype.capacity === 0) return;
    this.ships.splice(0, 0, ShipDto.fromShipPrototypeDto(this.newShipPrototype));
    this.newShipPrototype = new ShipPrototypeDto('', 0, true);
    // Todo send to backend
  }



  deleteShip(ship: ShipDto | undefined = undefined) {
    console.log(ship)
    if(ship === undefined) return;
    this.ships = this.ships.filter(s => s.id !== ship.id);
    // Todo send to backend
  }



  editShip(ship: ShipDto | undefined) {
    console.log(ship)
    if (ship === undefined) return;
    this.ships = this.ships.map(s => s.id === ship.id ? ship : s);
    // Todo send to backend
  }
}
