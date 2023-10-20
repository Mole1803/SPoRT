import { ComponentFixture, TestBed } from '@angular/core/testing';

import { QuestTableComponent } from './quest-table.component';

describe('QuestTableComponent', () => {
  let component: QuestTableComponent;
  let fixture: ComponentFixture<QuestTableComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [QuestTableComponent]
    });
    fixture = TestBed.createComponent(QuestTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
