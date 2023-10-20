import { ComponentFixture, TestBed } from '@angular/core/testing';

import { QuestGridElementComponent } from './quest-grid-element.component';

describe('QuestGridElementComponent', () => {
  let component: QuestGridElementComponent;
  let fixture: ComponentFixture<QuestGridElementComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [QuestGridElementComponent]
    });
    fixture = TestBed.createComponent(QuestGridElementComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
