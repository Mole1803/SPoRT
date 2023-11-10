import {Method} from "../enums/method";
import {Algorithm} from "../enums/algorithm";

export class AlgorithmChoice {
  algorithm: Algorithm
  method: Method
  constructor(algorithm: Algorithm,method: Method) {
    this.algorithm=algorithm;
    this.method=method;
  }
}
