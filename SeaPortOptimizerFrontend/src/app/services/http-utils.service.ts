import {Inject, Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class HttpUtilsService {

  constructor(private http: HttpClient, @Inject('BASE_URL') private baseUrl: string) {

  }

  register(username: string, password: string) {
    return this.http.post(this.baseUrl+"/auth/register", {username: username, password: password});
  }

  login(username: string, password: string) {
    return this.http.post(this.baseUrl+"/auth/login", {username: username, password: password});
  }

  jwtTokenTest(){
    return this.http.get(this.baseUrl+"/auth/test_jwt");
  }

  isBackendAlive() {
    return this.http.get(this.baseUrl+"/isAlive");
  }
}
