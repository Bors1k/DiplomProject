import { AfterViewInit, Component, ElementRef, Input, OnInit, TemplateRef, ViewChild } from '@angular/core';

@Component({
  selector: 'app-gost-element',
  templateUrl: './gost-element.component.html',
  styleUrls: ['./gost-element.component.css']
})
export class GOSTElementComponent implements OnInit, AfterViewInit {

  @Input() gost;
  @ViewChild('gostElement') gostElem: ElementRef<any>;
  
  headers = ["GOST", "TYPE", "INFO"];
  routerLink: string;
  
  constructor() {
    // console.log(this.gost)
    // console.log(this.gost.MODEL_URL)
    // if(this.gost.MODEL_URL == 'none'){
    //   this.gostElem.nativeElement.style = "display: hidden;"
    // }
  }
  ngAfterViewInit(){
    // if(this.gost.MODEL_URL == 'none'){
    //   this.gostElem.nativeElement
    //   this.gostElem.nativeElement.style = "display: hidden;"
    // }
  }

  ngOnInit(): void {
    console.log(this.gost)
    this.routerLink = "/" + this.gost[this.headers[0]] + "/" + this.gost[this.headers[1]];
    // console.log(this.gost.MODEL_URL)
    // if(this.gost.MODEL_URL == 'none'){
    //   this.gostElem.nativeElement.style = "display: hidden;"
    // }  
  }

}
