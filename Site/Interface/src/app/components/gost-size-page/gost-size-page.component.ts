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
  GostSizes: any[];
  model_url: string;
  pic_url: string;

  GOST: any;
  TYPE: any;

  constructor(private rout: ActivatedRoute, private gostsService: GostsService) {
    this.rout.paramMap.subscribe(params => {
      this.GOST = params.get("GOST");
      this.TYPE = params.get("TYPE");
    })
  }

   async ngOnInit() {
    await this.getTypeGOSTS(this.GOST, this.TYPE);
  }

  async getTypeGOSTS(GOST, TYPE) {
    try {
      this.GostSizes = await this.gostsService.getGostSizes(GOST, TYPE);
      let GostRow = (await this.gostsService.getGostRow(GOST,TYPE))[0];

      this.model_url = GostRow["MODEL_URL"]
      this.pic_url = GostRow["PIC_URL"]

      let GostSize = this.GostSizes[0];
      for(var key in GostSize){
        if(GostSize.hasOwnProperty(key)){
          if(key != "GOST")
          this.headers.push(key);
        }
      }
    }
    catch (err) {
      console.error(err);
    }
  }

  insertFile(GostSizes: any) {
      console.log(GostSizes);
      var properties = {
        "PartNumber": "",
        "PartName": this.GOST + " " + GostSizes.NUMBER,
        "Description": ""
      }
      window.location.href = "fusion360://command=insert&file=" + encodeURIComponent(this.model_url) +
        "&properties=" + encodeURIComponent(JSON.stringify(properties)) +
        "&privateInfo=" + encodeURIComponent(this.setString(GostSizes)) +
        "&id=" + encodeURIComponent(this.GOST + " " + GostSizes.NUMBER) + "&NoFit=true&NoMove=true"; //id будет формироваться как номергоста_номердетали
        //это строго необходимо, т.к. при импорте детали, eсли id у деталей равны, он просто делает копию, и они связаны становятся
        //сейчас это тек.дата как временная заглушка
    }
  
    setString(GostSizes) {
      var str = "";
      for(var key in GostSizes){
        if(GostSizes.hasOwnProperty(key)){
          if(key != "GOST" && key != "NUMBER")
          str+=GostSizes[key] + "/";
        }
      }
      return str.slice(0,-1);;
    }
}
