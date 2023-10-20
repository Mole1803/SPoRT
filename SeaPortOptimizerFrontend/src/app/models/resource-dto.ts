import {ModelBaseDto} from "./model-base-dto";

export class ResourceDto extends ModelBaseDto{
  picturePath: string;

  constructor(name: string, picturePath: string) {
    super(name);

    this.picturePath = picturePath;
  }
}
