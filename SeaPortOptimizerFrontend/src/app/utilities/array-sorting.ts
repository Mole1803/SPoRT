export class ArraySorting {
  static sortArrayAlphabetically(array: any[], property: string, isAscending: boolean): any[] {
    if(isAscending) {
      return array.sort((a, b) => a[property].localeCompare(b[property]));
    }
    else {
      return array.sort((a, b) => b[property].localeCompare(a[property]));
    }
  }

  static sortArrayNumerically(array: any[], property: string, isAscending: boolean): any[] {
    if(isAscending) {
      return array.sort((a, b) => a[property] - b[property]);
    }
    else {
      return array.sort((a, b) => b[property] - a[property]);
    }
  }

}
