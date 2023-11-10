import { TestBed } from '@angular/core/testing';

import { ResultHttpRequestService } from './result-http-request.service';

describe('ResultHttpRequestService', () => {
  let service: ResultHttpRequestService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ResultHttpRequestService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
