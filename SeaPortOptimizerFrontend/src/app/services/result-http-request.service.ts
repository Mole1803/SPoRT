import {HttpClient} from "@angular/common/http";
import {Inject, Injectable, Input} from "@angular/core";
import {from, Observable, of} from "rxjs";
import {Result} from "../models/result";
import {Round} from "../models/round";
import {Step} from "../models/step";

@Injectable({
  providedIn: 'root'
})

export class ResultHttpRequestService {

  constructor(private http: HttpClient, @Inject('BASE_URL') private baseUrl: string) {

  }

  getResult(algo: string, method: string): Observable<Result[]>{
    return this.http.post<Result[]>(this.baseUrl + "/solve", {developer: algo, algorithm: method})
  }
}
