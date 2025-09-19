import { Component, Input } from '@angular/core';
import { MatProgressBarModule } from '@angular/material/progress-bar';

@Component({
  selector: 'app-progress-bar',
  imports: [MatProgressBarModule],
  templateUrl: './progress-bar.component.html',
  styleUrl: './progress-bar.component.scss'
})
export class ProgressBarComponent {
 /** Value of the progress (0-100) */
  @Input() value: number = 0;

  /** Optional color: primary, accent, warn */
  @Input() color: 'primary' | 'accent' | 'warn' = 'primary';

  /** Optional mode: determinate, indeterminate, buffer, query */
  @Input() mode: 'determinate' | 'indeterminate' | 'buffer' | 'query' = 'determinate';
}
