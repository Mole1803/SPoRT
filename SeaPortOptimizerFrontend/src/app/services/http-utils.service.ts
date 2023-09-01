import {Inject, Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class HttpUtilsService {

  constructor(private http: HttpClient, @Inject('BASE_URL') private baseUrl: string) {

  }

  isBackendAlive() {
    return this.http.get(this.baseUrl+"/isAlive");
  }
}
