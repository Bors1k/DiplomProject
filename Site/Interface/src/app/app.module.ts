import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SearchFilterPipe } from './pipes/search-filter.pipe';
import { GOSTElementComponent } from './components/gost-element/gost-element.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NavBarComponent } from './components/nav-bar/nav-bar.component';
import { GostElementsListComponent } from './components/gost-elements-list/gost-elements-list.component';
import { GostSizePageComponent } from './components/gost-size-page/gost-size-page.component';

@NgModule({
  declarations: [
    AppComponent,
    SearchFilterPipe,
    GOSTElementComponent,
    NavBarComponent,
    GostElementsListComponent,
    GostSizePageComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
