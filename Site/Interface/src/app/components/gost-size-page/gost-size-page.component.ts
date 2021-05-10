import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { GostsService } from 'src/app/services/gosts.service';

@Component({
  selector: 'app-gost-size-page',
  templateUrl: './gost-size-page.component.html',
  styleUrls: ['./gost-size-page.component.css']
})
export class GostSizePageComponent implements OnInit {

  headers = [];
  TypeGosts: any[];
  model_url: string;
  pic_url: string;

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
    //console.log(this.URLS[0]);
  }

  // async getGostUrls(GOST, ID){
  //   try{
  //     let urls = this.gostsService.getGostUrls(GOST,ID);
  //     this.URLS = await urls;
  //   }
  //   catch(err){
  //     console.error(err);
  //   }
  // }

  async getTypeGOSTS(GOST, ID) {
    try {
      let TypeGosts = this.gostsService.getGostParams(GOST, ID);
      this.TypeGosts = await TypeGosts;
      let urls = this.gostsService.getGostUrls(GOST,ID);
      let URLS = await urls;
      this.model_url = URLS[0]["MODEL_URL"]
      this.pic_url = URLS[0]["PIC_URL"]
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
