import { PageEvent } from "@angular/material/paginator";
import { Car, CarApiService } from "../../services/car-api.service";
import { Component, Input, OnInit } from "@angular/core";
import { CommonModule } from "@angular/common";
import { MatButtonModule } from "@angular/material/button";
import { MatFormFieldModule } from "@angular/material/form-field";
import { MatInputModule } from "@angular/material/input";
import { MatSelectModule } from "@angular/material/select";
import { PaginatorComponent } from "../../../../shared/components/paginator/paginator.component";
import { MatCardModule } from "@angular/material/card";
import { MatAutocompleteModule } from "@angular/material/autocomplete";
import { FormsModule } from "@angular/forms";


@Component({
  selector: 'app-car-data-view',
  standalone: true,
  imports: [
    CommonModule,
    MatCardModule,
    MatButtonModule,
    // Angular Material form controls
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    MatAutocompleteModule,
    FormsModule
  ],
  templateUrl: './car-data-view.component.html',  
  styleUrls: ['./car-data-view.component.scss']
})
export class CarDataViewComponent implements OnInit {
  @Input() cars: Car[] = [];
  ngOnInit(): void {}
}
