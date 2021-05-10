import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-gost-element',
  templateUrl: './gost-element.component.html',
  styleUrls: ['./gost-element.component.css']
})
export class GOSTElementComponent implements OnInit {

  @Input() gost;
  headers = ["GOST", "ID"];
  routerLink: string;
  
  constructor() {
   }

  ngOnInit(): void {
    // for(var  key in this.gost){
    //   if(this.gost.hasOwnProperty(key)){
    //     console.log(key);
    //     console.log(this.gost[key]);
    //   }
    // }
    this.routerLink = "/" + this.gost[this.headers[0]] + "/" + this.gost[this.headers[1]];
    console.log(this.gost);    
  }

}
