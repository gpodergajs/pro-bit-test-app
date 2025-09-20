import { NavigationEnd, Router, RouterOutlet } from "@angular/router";
import { filter } from "rxjs";
import { AuthService } from "../../../features/auth/services/auth.service";
import { CommonModule } from "@angular/common";
import { Component, inject } from "@angular/core";
import { MatButtonModule } from "@angular/material/button";
import { MatIconModule } from "@angular/material/icon";
import { MatToolbarModule } from "@angular/material/toolbar";
import {Location} from "@angular/common"

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [
    CommonModule,
    
    MatToolbarModule,
    MatButtonModule,
    MatIconModule,
  ],
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent {
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