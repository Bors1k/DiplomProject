import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GostSizePageComponent } from './gost-size-page.component';

describe('GostSizePageComponent', () => {
  let component: GostSizePageComponent;
  let fixture: ComponentFixture<GostSizePageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GostSizePageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GostSizePageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
