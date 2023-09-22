import { ComponentFixture, TestBed } from '@angular/core/testing';

import { QuestViewComponent } from './quest-view.component';

describe('QuestViewComponent', () => {
  let component: QuestViewComponent;
  let fixture: ComponentFixture<QuestViewComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [QuestViewComponent]
    });
    fixture = TestBed.createComponent(QuestViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
