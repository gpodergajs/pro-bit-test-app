import { Injectable, inject } from '@angular/core';

import { HttpErrorResponse } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class ErrorHandlingService {
  

   getErrorMessage(error: HttpErrorResponse): string {
    if (error.error instanceof ErrorEvent) {
      // Client-side/network error
      return `Network error: ${error.error.message}`;
    } else {
      // Backend returned an error response
      switch (error.status) {
        case 0:
          return 'Unable to connect to the server. Please try again later.';
        case 400:
          return error.error?.message || 'Invalid request. Please check your input.';
        case 401:
          return 'Unauthorized. Please log in again.';
        case 403:
          return 'You do not have permission to perform this action.';
        case 404:
          return 'Resource not found.';
        case 500:
          return 'Server error. Please try again later.';
        default:
          return error.error?.message || `Unexpected error (code: ${error.status}).`;
      }
    }
  }
}