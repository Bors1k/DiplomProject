import { Component, OnInit, Output,EventEmitter } from '@angular/core';
import { TreeviewService } from 'src/app/services/treeview.service';
import { MatTreeNestedDataSource } from '@angular/material/tree';
import { NestedTreeControl } from '@angular/cdk/tree';
import { PartsNode } from 'src/app/interfaces/PartsNode';

@Component({
  selector: 'app-tree-view-comp',
  templateUrl: './tree-view-comp.component.html',
  styleUrls: ['./tree-view-comp.component.css']
})

export class TreeViewComponent implements OnInit {

  @Output() selectCategoryEvent = new EventEmitter<PartsNode>();
  
  treeControl = new NestedTreeControl<PartsNode>(node => node.children)
  treeViewData = new MatTreeNestedDataSource<PartsNode>();
  
  constructor(private treeViewService: TreeviewService) { 
  }
  
  selectCategory(object: PartsNode){
    this.selectCategoryEvent.emit(object);
  }
  
  collapseAll(){
    this.treeControl.collapseAll()
    this.selectCategoryEvent.emit(null)
  }

  async ngOnInit() {
    let _treeViewData: PartsNode[];
    _treeViewData = await this.treeViewService.getTreeView()
    
    _treeViewData.forEach(element => {
      element.children = []
      element.childs!=null ? element.childs = element.childs.split("/"): false
    });
    _treeViewData.forEach(firstCicrle => {
      let i = 0;
      _treeViewData.forEach(secondCicrle => {
        if (firstCicrle.idTreeViewTable == secondCicrle.parent) {
          firstCicrle.children[i] = secondCicrle
          i++;
        }
      });
    });
    this.treeViewData.data = [_treeViewData[0]]
  }
  hasChild = (_:number, node: PartsNode)=>!!node.children && node.children.length > 0;
}