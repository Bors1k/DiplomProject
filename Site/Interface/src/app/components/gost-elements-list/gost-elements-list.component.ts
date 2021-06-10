import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { GostsService } from 'src/app/services/gosts.service';
import { IGostRow } from '../../interfaces/GOST';
import { PartsNode } from 'src/app/interfaces/PartsNode';

@Component({
  selector: 'app-gost-elements-list',
  templateUrl: './gost-elements-list.component.html',
  styleUrls: ['./gost-elements-list.component.css']
})
export class GostElementsListComponent implements OnInit {

  searchStr: string;
  selectedCategory: PartsNode;
  gosts: IGostRow[];

  @ViewChild('searchInput') searchInput: ElementRef;
  
  constructor(private gostsService: GostsService) { }

  changeSearchStr(){
    this.searchStr = this.searchInput.nativeElement.value;
  }

  changeSelectedCategory(object: PartsNode){
    this.selectedCategory = object;
  }

  async ngOnInit(){
    try{
      let gosts = this.gostsService.getAllGosts()
      this.gosts = await gosts;
      this.gosts = this.gosts.filter((gost)=>{
          if(gost.MODEL_URL != "none"){
            return gost
          }
      })
    }
    catch(err){
      console.error(err);
    }
  }
}
