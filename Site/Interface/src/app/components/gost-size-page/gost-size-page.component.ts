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
  }

  async getTypeGOSTS(GOST, ID) {
    try {
      this.TypeGosts = await this.gostsService.getGostParams(GOST, ID);
      let URLS = await this.gostsService.getGostUrls(GOST,ID);

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

  insertFile(TypeGost: any) {
      console.log(TypeGost);
      var properties = {
        "PartNumber": "",
        "PartName": this.GOST + " " + TypeGost.NUMBER,
        "Description": ""
      }
      window.location.href = "fusion360://command=insert&file=" + encodeURIComponent(this.model_url) +
        "&properties=" + encodeURIComponent(JSON.stringify(properties)) +
        "&privateInfo=" + encodeURIComponent(this.setString(TypeGost)) +
        "&id=" + encodeURIComponent(this.GOST + " " + TypeGost.NUMBER) + "&NoFit=true&NoMove=true"; //id будет формироваться как номергоста_номердетали
        //это строго необходимо, т.к. при импорте детали, eсли id у деталей равны, он просто делает копию, и они связаны становятся
        //сейчас это тек.дата как временная заглушка
    }
  
    setString(TypeGost) {
      var str = "";
      for(var key in TypeGost){
        if(TypeGost.hasOwnProperty(key)){
          if(key != "GOST" && key != "NUMBER")
          str+=TypeGost[key] + "/";
        }
      }
      console.log(str.slice(0,-1));
      return str.slice(0,-1);;
    }
}
