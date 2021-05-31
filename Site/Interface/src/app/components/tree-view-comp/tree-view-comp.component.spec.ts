import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TreeViewCompComponent } from './tree-view-comp.component';

describe('TreeViewCompComponent', () => {
  let component: TreeViewCompComponent;
  let fixture: ComponentFixture<TreeViewCompComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TreeViewCompComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TreeViewCompComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
