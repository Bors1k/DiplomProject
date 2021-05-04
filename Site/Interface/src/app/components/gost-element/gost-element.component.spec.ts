import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GOSTElementComponent } from './gost-element.component';

describe('GOSTElementComponent', () => {
  let component: GOSTElementComponent;
  let fixture: ComponentFixture<GOSTElementComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GOSTElementComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GOSTElementComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
