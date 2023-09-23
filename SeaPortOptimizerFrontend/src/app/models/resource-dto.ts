export class ResourceDto {
  name: string;
  picturePath: string;

  constructor(name: string, picturePath: string) {
    this.name = name;
    this.picturePath = picturePath;
  }
}
