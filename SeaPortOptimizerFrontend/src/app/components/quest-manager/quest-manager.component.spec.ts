import { ComponentFixture, TestBed } from '@angular/core/testing';

import { QuestManagerComponent } from './quest-manager.component';

describe('QuestManagerComponent', () => {
  let component: QuestManagerComponent;
  let fixture: ComponentFixture<QuestManagerComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [QuestManagerComponent]
    });
    fixture = TestBed.createComponent(QuestManagerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
