import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { GostsService } from 'src/app/services/gosts.service';

@Component({
  selector: 'app-data-table',
  templateUrl: './data-table.component.html',
  styleUrls: ['./data-table.component.css']
})
export class DataTableComponent implements OnInit {

  headers = [];
  TypeGosts: any[];

  GOST: any;
  ID: any;

  constructor(private rout: ActivatedRoute, private gostsService: GostsService) {
    this.rout.paramMap.subscribe(params => {
      this.GOST = params.get("GOST");
      this.ID = params.get("ID");
    })
  }

   async ngOnInit() {
    await this.getTypeGOSTS(this.GOST, this.ID);
    console.log(this.TypeGosts);
  }

  async getTypeGOSTS(GOST, ID) {
    try {
      let TypeGosts = this.gostsService.getGostParams(GOST, ID)
      this.TypeGosts = await TypeGosts;
      let TypeGost = this.TypeGosts[0];
      for(var key in TypeGost){
        if(TypeGost.hasOwnProperty(key)){
          if(key != "GOST")
          this.headers.push(key);
        }
      }
    }
    catch (err) {
      console.error(err);
    }
  }

}
