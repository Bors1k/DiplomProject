import { Component, OnInit } from '@angular/core';
import { TreeviewService } from 'src/app/services/treeview.service';
import { MatTreeNestedDataSource } from '@angular/material/tree';
import { NestedTreeControl } from '@angular/cdk/tree';
import { massive } from './json.json'

interface PartsNode {
  idTreeViewTable: any;
  name: string;
  parent: any;
  children?: PartsNode[];
}

interface FoodNode {
  name: string;
  children?: FoodNode[];
}

const TREE_DATA: FoodNode[] = [
  {
    name: 'Fruit',
    children: [
      {name: 'Apple'},
      {name: 'Banana'},
      {name: 'Fruit loops'},
    ]
  }, {
    name: 'Vegetables',
    children: [
      {
        name: 'Green',
        children: [
          {name: 'Broccoli'},
          {name: 'Brussels sprouts'},
        ]
      }, {
        name: 'Orange',
        children: [
          {name: 'Pumpkins'},
          {name: 'Carrots'},
        ]
      },
    ]
  },
];

@Component({
  selector: 'app-tree-view-comp',
  templateUrl: './tree-view-comp.component.html',
  styleUrls: ['./tree-view-comp.component.css']
})
export class TreeViewCompComponent {

  treeControl = new NestedTreeControl<PartsNode>(node => node.children)
  treeViewData = new MatTreeNestedDataSource<PartsNode>();
  jsondata: any;

  constructor(private treeViewService: TreeviewService) { 
    // console.log(TREE_DATA)
    // console.log(massive)
    // this.treeViewData.data = 
    this.OnInit()
  }

  async OnInit() {
    let treeViewData: PartsNode[];
    treeViewData = await this.treeViewService.getTreeView()

    treeViewData.forEach(element => {
      let children: PartsNode[] = [];
      element.children = children
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
    console.log(treeViewData[0])
    this.treeViewData.data = [treeViewData[0]]
    // this.treeViewData.data = treeViewData[]
    // console.log(this.treeViewData.data)
  }

  hasChild = (_:number, node: PartsNode)=>!!node.children && node.children.length > 0;

}
