import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { GostsService } from 'src/app/services/gosts.service';

@Component({
  selector: 'app-gost-elements-list',
  templateUrl: './gost-elements-list.component.html',
  styleUrls: ['./gost-elements-list.component.css']
})
export class GostElementsListComponent implements OnInit {

  searchStr: string;
  gosts: any[];
  gost: any;
  TypeGosts: any[];

  @ViewChild('searchInput') searchInput: ElementRef;
  
  constructor(private gostsService: GostsService) { }

  changeSearchStr(){
    this.searchStr = this.searchInput.nativeElement.value;
  }

  async ngOnInit(){
    await this.getGosts();
  }

  async getGosts(){
    try{
      let gosts = this.gostsService.getAllGosts()
      this.gosts = await gosts;
    }
    catch(err){
      console.error(err);
    }
  }
}
