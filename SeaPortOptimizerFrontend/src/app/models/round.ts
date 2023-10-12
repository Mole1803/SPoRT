import {Step} from "./step";

export class Round {
  steps: Step[];

  constructor(steps: Step[]) {
    this.steps = steps;
  }
}
