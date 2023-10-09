import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShipTableComponent } from './ship-table.component';

describe('ShipTableComponent', () => {
  let component: ShipTableComponent;
  let fixture: ComponentFixture<ShipTableComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ShipTableComponent]
    });
    fixture = TestBed.createComponent(ShipTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
