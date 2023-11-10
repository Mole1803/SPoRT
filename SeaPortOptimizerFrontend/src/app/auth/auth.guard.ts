import {CanActivateFn, Router} from '@angular/router';
import {inject} from "@angular/core";
import {AuthService} from "./auth.service";
import {AppRoutes} from "../enums/app-routes";

export const authGuard: CanActivateFn = (route, state) => {
  const authService = inject(AuthService)
  const router = inject(Router)
  if(authService.isAuthenticated()){
    return true
  }
  return router.parseUrl("/"+AppRoutes.LOGIN)
};
