import { PageEvent } from "@angular/material/paginator";
import { Car, CarApiService } from "../../services/car-api.service";
import { Component, Input, OnInit, SimpleChanges } from "@angular/core";
import { CommonModule } from "@angular/common";
import { MatButtonModule } from "@angular/material/button";
import { MatFormFieldModule } from "@angular/material/form-field";
import { MatInputModule } from "@angular/material/input";
import { MatSelectModule } from "@angular/material/select";
import { PaginatorComponent } from "../../../../shared/components/paginator/paginator.component";
import { MatCardModule } from "@angular/material/card";
import { MatAutocompleteModule } from "@angular/material/autocomplete";
import { FormsModule } from "@angular/forms";
import { RouterLink } from "@angular/router";
import { AuthService } from "../../../auth/services/auth.service";
import { BreakpointObserver, Breakpoints } from '@angular/cdk/layout';
import { MatGridList, MatGridListModule } from '@angular/material/grid-list';


@Component({
  selector: 'app-car-data-view',
  standalone: true,
  imports: [
    CommonModule,
    MatCardModule,
    MatButtonModule,
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    MatAutocompleteModule,
    FormsModule,
    RouterLink,
    MatGridListModule
  ],
  templateUrl: './car-data-view.component.html',  
  styleUrls: ['./car-data-view.component.scss']
})
export class CarDataViewComponent implements OnInit {
  @Input() cars: Car[] = [];

  isAdmin: boolean = false;


  constructor(public authService: AuthService, private breakpointObserver: BreakpointObserver) {}

  ngOnInit(): void {
    this.isAdmin = this.authService.isAdmin();
  }

  
}
