import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditShipModalComponent } from './edit-ship-modal.component';

describe('EditShipModalComponent', () => {
  let component: EditShipModalComponent;
  let fixture: ComponentFixture<EditShipModalComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [EditShipModalComponent]
    });
    fixture = TestBed.createComponent(EditShipModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
