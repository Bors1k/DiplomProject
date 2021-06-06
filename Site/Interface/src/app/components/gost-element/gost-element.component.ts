import { Component, Input, OnInit } from '@angular/core';
import { IGostRow } from 'src/app/interfaces/GOST';

@Component({
  selector: 'app-gost-element',
  templateUrl: './gost-element.component.html',
  styleUrls: ['./gost-element.component.css']
})
export class GOSTElementComponent implements OnInit {

  @Input() gost: IGostRow;
  pic_url: string;
  
  headers = ["GOST", "TYPE", "INFO"];
  routerLink: string;
  
  constructor() {
  }

  ngOnInit(): void {
    this.routerLink = "/" + this.gost[this.headers[0]] + "/" + this.gost[this.headers[1]];
    this.pic_url = (this.gost.PIC_URL.split(','))[0]
    console.log(this.pic_url)
  }

}
