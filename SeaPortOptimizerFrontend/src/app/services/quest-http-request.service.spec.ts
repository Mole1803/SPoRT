import { TestBed } from '@angular/core/testing';

import { QuestHttpRequestService } from './quest-http-request.service';

describe('QuestHttpRequestService', () => {
  let service: QuestHttpRequestService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(QuestHttpRequestService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
