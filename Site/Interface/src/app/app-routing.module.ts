import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { GostElementsListComponent } from './components/gost-elements-list/gost-elements-list.component';
import { GostSizePageComponent } from './components/gost-size-page/gost-size-page.component';


const routes: Routes = [
  {path: '', component: GostElementsListComponent},
  {path: ':GOST/:ID', component: GostSizePageComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
