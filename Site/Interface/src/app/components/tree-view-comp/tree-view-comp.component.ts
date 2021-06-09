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

export class TreeViewCompComponent implements OnInit {

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
    let treeViewData: PartsNode[];
    treeViewData = await this.treeViewService.getTreeView()

    treeViewData.forEach(element => {
      element.children = []
      element.childs!=null ? element.childs = element.childs.split("/"): false
    });
    treeViewData.forEach(firstCicrle => {
      let i = 0;
      treeViewData.forEach(secondCicrle => {
        if (firstCicrle.idTreeViewTable == secondCicrle.parent) {
          firstCicrle.children[i] = secondCicrle
          i++;
        }
      });
    });
    this.treeViewData.data = [treeViewData[0]]
  }
  hasChild = (_:number, node: PartsNode)=>!!node.children && node.children.length > 0;
}