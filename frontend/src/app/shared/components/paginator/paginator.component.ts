import { Component, EventEmitter, Input, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatPaginatorModule, PageEvent } from '@angular/material/paginator';

@Component({
  selector: 'app-paginator',
  standalone: true,
  imports: [CommonModule, MatPaginatorModule],
  templateUrl: './paginator.component.html',
  styleUrls: ['./paginator.component.scss']
})
export class PaginatorComponent {
  @Input() length = 0;
  @Input() pageSize = 10;
  @Input() pageSizeOptions = [5, 10, 25, 100];

  @Output() page = new EventEmitter<PageEvent>();

  onPageChange(event: PageEvent) {
    this.page.emit(event);
  }
}