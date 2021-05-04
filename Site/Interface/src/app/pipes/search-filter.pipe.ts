import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'searchFilter'
})
export class SearchFilterPipe implements PipeTransform {

  transform(gosts: any, searchStr: string): any {
    if(gosts === undefined || gosts.length == 0 || searchStr == "" || searchStr === undefined){
      return gosts;
    }
    return gosts.filter(gost=>{
      if(gost.GOST.indexOf(searchStr)>=0){
        return true;
      }
      else return false;
    });
  }

}
