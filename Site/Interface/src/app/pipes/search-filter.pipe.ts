import { Pipe, PipeTransform } from '@angular/core';
import { PartsNode } from 'src/app/interfaces/PartsNode';

@Pipe({
  name: 'searchFilter'
})
export class SearchFilterPipe implements PipeTransform {

  transform(gosts: any, searchStr: string, NodePart: PartsNode): any {
    if ((gosts === undefined || gosts.length == 0 || searchStr == "" 
    || searchStr === undefined) && (NodePart == undefined || NodePart.idTreeViewTable == 1)) {
      return gosts;
    }
    return gosts.filter(gost => {
      if (searchStr == undefined || searchStr == '') {
        if (NodePart.childs != null && (gost.TREE_VIEW_ID == NodePart.idTreeViewTable 
          || NodePart.childs.includes(gost.TREE_VIEW_ID.toString()))) {
          return true;
        }
      }
      else if ((NodePart == undefined || gost.TREE_VIEW_ID == NodePart.idTreeViewTable
        || NodePart.idTreeViewTable == 1 || NodePart.childs.includes(gost.TREE_VIEW_ID.toString())) &&
        (gost.GOST.toLowerCase().indexOf(searchStr.toLowerCase()) >= 0 ||
          gost.INFO.toLowerCase().indexOf(searchStr.toLowerCase()) >= 0 ||
          gost.TYPE.toLowerCase().indexOf(searchStr.toLowerCase()) >= 0)) {
        return true;
      }
      else return false;
    });
  }
}
