import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HarborComponentComponent } from './harbor-component.component';

describe('HarborComponentComponent', () => {
  let component: HarborComponentComponent;
  let fixture: ComponentFixture<HarborComponentComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [HarborComponentComponent]
    });
    fixture = TestBed.createComponent(HarborComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
