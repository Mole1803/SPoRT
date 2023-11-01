import {Inject, Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {QuestDto} from "../models/quest-dto";

@Injectable({
  providedIn: 'root'
})
export class QuestHttpRequestService {

  constructor(private http: HttpClient, @Inject('BASE_URL') private baseUrl: string) { }

  getQuest(id: number) {
    return this.http.get(this.baseUrl+"/quest/get"+id);
  }

  list(): Observable<QuestDto[]> {
    return this.http.get<QuestDto[]>(this.baseUrl+"/quest/list");
  }

  addQuest(quest: any) {
    return this.http.post(this.baseUrl+"/quest/add", quest);
  }

  deleteQuest(quest: any) {
    return this.http.post(this.baseUrl+"/quest/delete", quest);
  }

  updateQuest(quest: any) {
    return this.http.post(this.baseUrl+"/quest/update", quest);
  }
}
