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
  
  routerLink: string;
  
  constructor() {
  }

  ngOnInit(): void {
    this.routerLink = "/" + this.gost.GOST + "/" + this.gost.TYPE;
    this.pic_url = (this.gost.PIC_URL.split(','))[0]
  }

}
