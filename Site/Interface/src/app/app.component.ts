import { ViewportScroller } from '@angular/common';
import { Component, ElementRef, Type, ViewChild } from '@angular/core';
// import { GostsService } from './services/gosts.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'GOST components library';

  constructor(private scroll: ViewportScroller){

  }

  scrollToTop(){
    this.scroll.scrollToPosition([0,0]);
  }
}
