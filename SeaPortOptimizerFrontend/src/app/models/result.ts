import {Round} from "./round";

export class Result {
  rounds: Round[];

  constructor(rounds: Round[]) {
    this.rounds = rounds;
  }
}
