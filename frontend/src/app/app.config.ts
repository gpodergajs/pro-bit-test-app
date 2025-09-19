import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';
import { providePrimeNG } from 'primeng/config';
import Lara from '@primeuix/themes/lara';

import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [provideZoneChangeDetection({ eventCoalescing: true }), provideRouter(routes),
        providePrimeNG({
            theme: {
                preset: Lara,
                options: {
                    prefix: 'p',
            darkModeSelector: false || 'none'
                    
                }
            }
        })]
};
