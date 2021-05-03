import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'searchFilter'
})
export class SearchFilterPipe implements PipeTransform {

  transform(gostsList: any[], searchStr: string): any {
    console.log(searchStr);
    if(gostsList.length === 0 || searchStr === ""){
      return gostsList;
    }
    return gostsList.filter(gost=>{
      if(gost.GOST.indexOf(searchStr)>=0){
        return true;
      }
      else return false;
    });
  }

}
