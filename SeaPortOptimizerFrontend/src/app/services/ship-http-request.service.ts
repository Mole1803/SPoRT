import {Inject, Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {ShipDto} from "../models/ship-dto";

@Injectable({
  providedIn: 'root'
})
export class ShipHttpRequestService {

  constructor(private http: HttpClient, @Inject('BASE_URL') private baseUrl: string) { }

  getShip(id: number) {
    return this.http.get(this.baseUrl+"/ship/get"+id);
  }

  list(): Observable<ShipDto[]> {
    return this.http.get<ShipDto[]>(this.baseUrl+"/ship/list");
  }

  addShip(ship: any) {
    return this.http.post(this.baseUrl+"/ship/add", ship);
  }

  deleteShip(ship: any) {
    return this.http.post(this.baseUrl+"/ship/delete", ship);
  }

  updateShip(ship: ShipDto) {
    return this.http.post(this.baseUrl+"/ship/update", ship);
  }
}
