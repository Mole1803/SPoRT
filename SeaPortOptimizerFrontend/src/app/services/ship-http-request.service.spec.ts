import { TestBed } from '@angular/core/testing';

import { ShipHttpRequestService } from './ship-http-request.service';

describe('ShipHttpRequestService', () => {
  let service: ShipHttpRequestService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ShipHttpRequestService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
