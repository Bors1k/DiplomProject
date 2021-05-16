import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-gost-element',
  templateUrl: './gost-element.component.html',
  styleUrls: ['./gost-element.component.css']
})
export class GOSTElementComponent implements OnInit {

  @Input() gost;
  headers = ["GOST", "TYPE"];
  routerLink: string;
  
  constructor() {}

  ngOnInit(): void {
    this.routerLink = "/" + this.gost[this.headers[0]] + "/" + this.gost[this.headers[1]];
  }

}
