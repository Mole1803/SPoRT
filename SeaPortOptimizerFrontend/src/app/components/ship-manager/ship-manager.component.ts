import {Component, Input} from '@angular/core';
import {ShipDto} from "../../models/ship-dto";
import {ShipPrototypeDto} from "../../models/ship-prototype-dto";
import {GuidGenerator} from "../../utilities/guid-generator";
import {EditModalService} from "../../services/edit-modal.service";
import {ModalMode} from "../../enums/modal-mode";
import {ShipHttpRequestService} from "../../services/ship-http-request.service";

@Component({
  selector: 'app-ship-manager',
  templateUrl: './ship-manager.component.html',
  styleUrls: ['./ship-manager.component.css']
})
export class ShipManagerComponent {
  @Input() ships: ShipDto[] = [];
  newShipPrototype: ShipPrototypeDto = new ShipPrototypeDto('', 0, true);


  constructor(public editModalService: EditModalService, public shipHttpRequestService: ShipHttpRequestService) {
    this.editModalService.reset();

    editModalService.confirmationEmitter.subscribe((ship: ShipDto | undefined) => {
        if (ship === undefined) return;
        if (editModalService.mode === ModalMode.EDIT) this.editShip(ship);
        if (editModalService.mode === ModalMode.DELETE) this.deleteShip(ship);

      }
    )
    this.fetchShipDto()
  }

  fetchShipDto() {
    this.shipHttpRequestService.list().subscribe((params => {
      this.ships = params
    }))

  }


  openEditModal(ship: ShipDto) {
    this.editModalService.mode = ModalMode.EDIT;
    this.editModalService._open(Object.assign({}, ship));
  }

  openDeleteModal(ship: ShipDto) {
    this.editModalService.mode = ModalMode.DELETE;
    this.editModalService._open(ship);
  }

  async addNewShip() {
    if (this.newShipPrototype.name === '' || this.newShipPrototype.capacity < 1) return;
    let ship = ShipDto.fromShipPrototypeDto(this.newShipPrototype)
    this.ships.splice(0, 0, ship);
    let result = await this.shipHttpRequestService.addShip(ship)
    result.subscribe()
    this.newShipPrototype = new ShipPrototypeDto('', 0, true);
  }


  deleteShip(ship: ShipDto | undefined = undefined) {
    if (ship === undefined) return;
    this.shipHttpRequestService.deleteShip(ship).subscribe()
    this.ships = this.ships.filter(s => s.id !== ship.id);
  }


  async editShip(ship: ShipDto | undefined) {
    if (ship === undefined) return;
    let result = await this.shipHttpRequestService.updateShip(ship)
    result.subscribe()
    this.ships = this.ships.map(s => s.id === ship.id ? ship : s);
  }
}
