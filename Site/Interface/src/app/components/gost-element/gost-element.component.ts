import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-gost-element',
  templateUrl: './gost-element.component.html',
  styleUrls: ['./gost-element.component.css']
})
export class GOSTElementComponent implements OnInit {

  @Input() gost: { GOST: string, TYPE: string, PIC_URL: string };
  
  constructor() { }

  ngOnInit(): void {
  }

}
