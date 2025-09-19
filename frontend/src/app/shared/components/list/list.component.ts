import { CommonModule } from '@angular/common';
import { Component, Input, TemplateRef } from '@angular/core';
import { MatListModule } from '@angular/material/list';

@Component({
  selector: 'app-list',
  imports: [CommonModule, MatListModule],  // ✅ important
  standalone: true,
  templateUrl: './list.component.html',
  styleUrl: './list.component.scss'
})
export class ListComponent {
    @Input() items: any[] = [];
  @Input() itemTemplate!: TemplateRef<any>;

}
