// src/app/auth/auth.service.ts
import { Injectable } from '@angular/core';
import {jwtDecode} from 'jwt-decode'




@Injectable()
export class AuthService {
  constructor() {}
  public isAuthenticated(): boolean {
    const token = localStorage.getItem('token');
    if (typeof token === "string") {
      let body = jwtDecode(token)
      if (Date.now() < body.exp!*1000) {
        return true
      }
    }
    return false
  }
}
