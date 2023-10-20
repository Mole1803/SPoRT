export class Tab {
  name: string;
  route: string;
  active: boolean;
  header?: boolean;
  footer: boolean = true;


  constructor(name: string, route: string, active: boolean, header?: boolean, footer?: boolean) {
    this.name = name;
    this.route = route;
    this.active = active;
  }
}
