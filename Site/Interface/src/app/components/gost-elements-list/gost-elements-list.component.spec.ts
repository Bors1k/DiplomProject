import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GostElementsListComponent } from './gost-elements-list.component';

describe('GostElementsListComponent', () => {
  let component: GostElementsListComponent;
  let fixture: ComponentFixture<GostElementsListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GostElementsListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GostElementsListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
