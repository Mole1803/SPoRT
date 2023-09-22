export class Tab {
  name: string;
  route: string;
  active: boolean;

  constructor(name: string, route: string, active: boolean) {
    this.name = name;
    this.route = route;
    this.active = active;
  }
}
