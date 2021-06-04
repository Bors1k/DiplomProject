import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'searchFilter'
})
export class SearchFilterPipe implements PipeTransform {

  transform(gosts: any, searchStr: string, categoryID: number): any {
    if((gosts === undefined || gosts.length == 0 || searchStr == "" || searchStr === undefined) && (categoryID == 1 || categoryID == undefined)){
      // console.log('returns all')
      return gosts;
    }
    return gosts.filter(gost=>{
      if(searchStr==undefined || searchStr==''){
        if(gost.TREE_VIEW_ID==categoryID){
          // console.log('returns categoryID')
          return true;
        }
      }
      else if((gost.TREE_VIEW_ID == categoryID || categoryID == 1) && (gost.GOST.toLowerCase().indexOf(searchStr.toLowerCase())>=0 || 
      gost.INFO.toLowerCase().indexOf(searchStr.toLowerCase())>=0 || 
      gost.TYPE.toLowerCase().indexOf(searchStr.toLowerCase())>=0))
      {
        // console.log('returns categoryID and searchSTR ')
        return true;
      }
      else return false;
    });
  }
}
