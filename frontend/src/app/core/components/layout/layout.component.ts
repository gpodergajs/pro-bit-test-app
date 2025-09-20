import { NavigationEnd, Router, RouterOutlet } from "@angular/router";
import { filter } from "rxjs";
import { AuthService } from "../../../features/auth/services/auth.service";
import { CommonModule } from "@angular/common";
import { Component, inject } from "@angular/core";
import { MatButtonModule } from "@angular/material/button";
import { MatIconModule } from "@angular/material/icon";
import { MatListModule } from "@angular/material/list";
import { MatSidenavModule } from "@angular/material/sidenav";
import { MatToolbarModule } from "@angular/material/toolbar";
import {Location} from "@angular/common"

@Component({
  selector: 'app-layout',
  standalone: true,
  imports: [
    CommonModule,
    RouterOutlet,
    MatToolbarModule,
    MatButtonModule,
    MatIconModule,
    MatSidenavModule,
    MatListModule
  ],
  templateUrl: './layout.component.html',
  styleUrls: ['./layout.component.scss']
})
export class LayoutComponent {
  private location = inject(Location);
  private authService = inject(AuthService);
  private router = inject(Router);

  currentUrl = '/';

  constructor() {
    this.router.events
      .pipe(filter(event => event instanceof NavigationEnd))
      .subscribe((event: NavigationEnd) => {
        this.currentUrl = event.urlAfterRedirects;
      });
  }
  
  goBack() {
    if (this.showBackButton()) {
      this.location.back();
    }
  }

  showBackButton(): boolean {
    // Hide back button on login, cars list, and root pages
    return !['/login', '/cars', '/'].includes(this.currentUrl);
  }

  showLogoutButton(): boolean {
    // Show logout button on all pages except login
    return this.currentUrl !== '/login';
  }

  logout() {
    this.authService.logout();
    this.router.navigate(['/login']);
  }
}
