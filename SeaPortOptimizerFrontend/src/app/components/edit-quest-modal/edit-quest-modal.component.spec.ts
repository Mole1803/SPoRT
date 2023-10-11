import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditQuestModalComponent } from './edit-quest-modal.component';

describe('EditQuestModalComponent', () => {
  let component: EditQuestModalComponent;
  let fixture: ComponentFixture<EditQuestModalComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [EditQuestModalComponent]
    });
    fixture = TestBed.createComponent(EditQuestModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
