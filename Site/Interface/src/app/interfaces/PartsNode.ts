export interface PartsNode {
  idTreeViewTable: number;
  name: string;
  parent: number;
  children?: PartsNode[];
  childs?: any;
}