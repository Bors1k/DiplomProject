import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BaseApiService } from './base-api.service';

@Injectable({
  providedIn: 'root'
})
export class GostsService extends BaseApiService {

  options: HttpHeaders;
  constructor(public http: HttpClient) {
    super(http);
    this.options = new HttpHeaders();
    this.options = this.options.set("Content-Type", "application/json");
  }

  getAllGosts() {
    return this.get('/GOSTS', this.options).toPromise();
  }

  getGostSizes(gost: string, type: string) {
    return this.get(`/GOSTS/${gost}/${type}/SIZES`, this.options).toPromise();
  }

  getGostRow(gost: string, type: string) {
    return this.get(`/GOSTS/${gost}/${type}`, this.options).toPromise();
  }
  getSizeHeaders(id: number) {
    return this.get(`/HEADERS/${id}`, this.options).toPromise();
  }
}
