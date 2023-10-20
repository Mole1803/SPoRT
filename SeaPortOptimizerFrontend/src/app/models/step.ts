export class Step {
  shipId: string
  questId: string
  usedCapacity: number

  constructor(shipId: string, questId: string, usedCapacity: number) {
    this.shipId = shipId
    this.questId = questId
    this.usedCapacity = usedCapacity
  }
}
