import { v4 as uuidv4 } from 'uuid';

export class GuidGenerator {

  static newGuidV4(): string {
    return uuidv4();
  }
}
