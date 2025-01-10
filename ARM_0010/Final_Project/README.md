# Greenhouse Monitoring API

A Django REST API to monitor and manage key metrics for a greenhouse farming system. This project provides authentication, CRUD operations for greenhouse metrics, and user-specific alert thresholds.

## Features

- **Authentication**: Secure API endpoints using token-based authentication.
- **CRUD Operations**: Create, retrieve, update, and delete greenhouse metrics (Temperature, Humidity, Soil Moisture, Light Level).
- **User Settings**: Users can set their threshold alerts for greenhouse metrics.
- **Pagination & Filtering**: List greenhouse metrics with pagination and filtering options.
- **Browsable API**: DRF's browsable API interface for easy testing and debugging.
  
## Requirements

- Python 3.8 or higher
- Django 4.2.6
- Django REST Framework 3.14.0
- django-filter 23.1
- djangorestframework-simplejwt 5.2.2
