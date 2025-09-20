import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CarDataViewComponent } from './car-data-view.component';

describe('CarDataViewComponent', () => {
  let component: CarDataViewComponent;
  let fixture: ComponentFixture<CarDataViewComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CarDataViewComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CarDataViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
