import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShipManagerComponent } from './ship-manager.component';

describe('ShipManagerComponent', () => {
  let component: ShipManagerComponent;
  let fixture: ComponentFixture<ShipManagerComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ShipManagerComponent]
    });
    fixture = TestBed.createComponent(ShipManagerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
