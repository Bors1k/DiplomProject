import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'searchFilter'
})
export class SearchFilterPipe implements PipeTransform {

  transform(gosts: any, searchStr: string, categoryID: number): any {
    if((gosts === undefined || gosts.length == 0 || searchStr == "" || searchStr === undefined) && (categoryID == 1 || categoryID == undefined)){
      return gosts;
    }
    return gosts.filter(gost=>{
      if(searchStr==undefined || searchStr==''){
        if(gost.TREE_VIEW_ID==categoryID){
          return true;
        }
      }
      else if((gost.TREE_VIEW_ID == categoryID || categoryID == 1 || categoryID == undefined) && (gost.GOST.toLowerCase().indexOf(searchStr.toLowerCase())>=0 || 
      gost.INFO.toLowerCase().indexOf(searchStr.toLowerCase())>=0 || 
      gost.TYPE.toLowerCase().indexOf(searchStr.toLowerCase())>=0))
      {
        return true;
      }
      else return false;
    });
  }
}
