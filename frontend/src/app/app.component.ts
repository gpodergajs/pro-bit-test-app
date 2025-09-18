import { Component, ElementRef, ViewChild } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Toast } from 'bootstrap';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
 @ViewChild('myToast', { static: true }) toastEl!: ElementRef<HTMLDivElement>;
  toastInstance!: Toast;

  ngAfterViewInit() {
    this.toastInstance = new Toast(this.toastEl.nativeElement);
  }

  showToast() {
    this.toastInstance.show();
  }

  hideToast() {
    this.toastInstance.hide();
  }
}
