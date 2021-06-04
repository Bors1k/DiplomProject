import { Component, OnInit, Output,EventEmitter } from '@angular/core';
import { TreeviewService } from 'src/app/services/treeview.service';
import { MatTreeNestedDataSource } from '@angular/material/tree';
import { NestedTreeControl } from '@angular/cdk/tree';

interface PartsNode {
  idTreeViewTable: any;
  name: string;
  parent: any;
  children?: PartsNode[];
  childrensId?: number[];
}

@Component({
  selector: 'app-tree-view-comp',
  templateUrl: './tree-view-comp.component.html',
  styleUrls: ['./tree-view-comp.component.css']
})

export class TreeViewCompComponent {

  @Output() selectCategoryEvent = new EventEmitter<number>();


  treeControl = new NestedTreeControl<PartsNode>(node => node.children)
  treeViewData = new MatTreeNestedDataSource<PartsNode>();

  constructor(private treeViewService: TreeviewService) { 
    this.OnInit()
  }

  selectCategory(id: number){
    this.selectCategoryEvent.emit(id);
  }

  collapseAll(){
    this.treeControl.collapseAll()
    this.selectCategoryEvent.emit(1)
  }
  
  async OnInit() {
    let treeViewData: PartsNode[];
    treeViewData = await this.treeViewService.getTreeView()

    treeViewData.forEach(element => {
      element.children = []
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