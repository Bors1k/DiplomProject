import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SearchFilterPipe } from './pipes/search-filter.pipe';
import { GOSTElementComponent } from './components/gost-element/gost-element.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NavBarComponent } from './components/nav-bar/nav-bar.component';
import { GostElementsListComponent } from './components/gost-elements-list/gost-elements-list.component';
import { GostSizePageComponent } from './components/gost-size-page/gost-size-page.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { TreeViewComponent } from './components/tree-view-comp/tree-view-comp.component';

import { MatNativeDateModule } from '@angular/material/core';
import { MAT_FORM_FIELD_DEFAULT_OPTIONS } from '@angular/material/form-field';
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
import { MatIconModule } from '@angular/material/icon'
import { MatTreeModule } from '@angular/material/tree'
import { MatButtonModule } from '@angular/material/button'

@NgModule({
  declarations: [
    AppComponent,
    SearchFilterPipe,
    GOSTElementComponent,
    NavBarComponent,
    GostElementsListComponent,
    GostSizePageComponent,
    TreeViewComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    BrowserAnimationsModule,
    NgbModule,
    ReactiveFormsModule,
    MatNativeDateModule,
    MatIconModule,
    MatTreeModule,
    MatButtonModule
  ],
  providers: [
    { provide: MAT_FORM_FIELD_DEFAULT_OPTIONS, useValue: { appearance: 'fill' } },],
  bootstrap: [AppComponent]
})
export class AppModule { }

platformBrowserDynamic().bootstrapModule(AppModule)
  .catch(err => console.error(err));