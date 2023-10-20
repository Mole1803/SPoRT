import { TestBed } from '@angular/core/testing';

import { EditModalService } from './edit-modal.service';

describe('EditModalService', () => {
  let service: EditModalService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EditModalService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
