import {Inject, Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class HttpUtilsService {

  constructor(private http: HttpClient, @Inject('BASE_URL') private baseUrl: string) {

  }

  login(username: string, password: string) {
    return this.http.post(this.baseUrl+"/login", {username: username, password: password});
  }

  isBackendAlive() {
    return this.http.get(this.baseUrl+"/isAlive");
  }

  getShips() {
    return this.http.get(this.baseUrl+"/getShips");
  }

  addShip(ship: any) {
    return this.http.post(this.baseUrl+"/addShip", ship);
  }


}
