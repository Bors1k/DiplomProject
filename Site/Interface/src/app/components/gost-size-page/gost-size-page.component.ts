import {  Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { GostsService } from 'src/app/services/gosts.service';
import { IGostRow } from '../../interfaces/GOST';


@Component({
  selector: 'app-gost-size-page',
  templateUrl: './gost-size-page.component.html',
  styleUrls: ['./gost-size-page.component.css']
})
export class GostSizePageComponent implements OnInit {


  headers = [];
  GostSizes: any[];
  model_url: string;
  pic_urls: string[];
  GostRow: IGostRow;
  DataSourse: any[];
  SizeHeaderDescriptions: any;

  private APP_UID = "3854bc50-bbcc-11eb-8529-0242ac130003"
  // private ModelsBaseLink = "http://localhost:4200/assets/models/"
  private ModelsBaseLink = "https://fusion-gost-library.web.app/assets/models/"

  GOST: any;
  TYPE: any;

  page = 1;
  pageSize = 20;
  collectionSize;

  constructor(private rout: ActivatedRoute, private gostsService: GostsService) {
    this.rout.paramMap.subscribe(params => {
      this.GOST = params.get("GOST");
      this.TYPE = params.get("TYPE");
    })
    this.GostRow = {
      ID: 1,
      GOST: "",
      TYPE: "",
      MODEL_URL: "",
      PIC_URL: "",
      INFO: "",
      TREE_VIEW_ID: null
    }
  }

  refreshParams() {
    this.DataSourse = this.GostSizes
      .map((row, i) => ({id: i + 1, ...row}))
      .slice((this.page - 1) * this.pageSize, (this.page - 1) * this.pageSize + this.pageSize);
  }
  

  async ngOnInit() {
    try {
      this.GostRow = (await this.gostsService.getGostRow(this.GOST,this.TYPE))[0];
      this.GostSizes = await this.gostsService.getGostSizes(this.GOST, this.TYPE);
      this.SizeHeaderDescriptions = (await this.gostsService.getSizeHeaders(this.GostRow.ID))[0].headers.split("/")
      this.model_url = this.GostRow["MODEL_URL"]
      this.pic_urls = this.GostRow["PIC_URL"].split(',')
      let GostSize = this.GostSizes[0];
      for(var key in GostSize){
        if(GostSize.hasOwnProperty(key)){
          if(key != "GOST")
          this.headers.push(key);
        }
      }
      this.collectionSize = this.GostSizes.length;
      this.refreshParams();
    }
    catch(err){
      console.error(err);
    }
  }

  insertFile(GostSizes: any) {

      var properties = {
        "PartNumber": "",
        "PartName": this.GOST + " " + GostSizes.NUMBER,
        "Description": "",
        "AppUID": this.APP_UID,
        "GOST": this.GOST,
        "TYPE": this.TYPE
      }

      var NavigationUrl = "fusion360://host/?command=insert&file=" + encodeURIComponent(this.ModelsBaseLink + this.model_url) +
      "&properties=" + encodeURIComponent(JSON.stringify(properties)) +
      "&privateInfo=" + encodeURIComponent(this.setPrivateInfo(GostSizes)) +
      "&id=" + encodeURIComponent(this.GOST + " " + GostSizes.NUMBER) + "&NoFit=true&NoMove=true";

      window.location.assign(NavigationUrl)
    }
  
    setPrivateInfo(GostSizes) {
      var str = "";
      for(var key in GostSizes){
        if(GostSizes.hasOwnProperty(key)){
          if(key != "GOST" && key != "NUMBER" && key != "id"){
            if(GostSizes[key]!='' && GostSizes[key]!='NULL' && GostSizes[key]!= null)
            str+=GostSizes[key] + "/";
          }
        }
      }
      return str.slice(0,-1);
    }
}