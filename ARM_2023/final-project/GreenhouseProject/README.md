# Final-Project

## Description
A Django-based API for managing greenhouse metrics. This project allows users to track temperature, humidity, and light intensity in a greenhouse environment.

## Features
- RESTful API for greenhouse metrics.
- User authentication.
- CRUD operations for metrics data.
- Automatic timestamps for data entries.

## Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd Final-Project
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Apply migrations:
   ```bash
   python manage.py migrate
   ```

## Usage
1. Start the development server:
   ```bash
   python manage.py runserver
   ```
2. Access the API at [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/).
3. Log in to the admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## API Endpoints
- **GET /api/metrics/**: Retrieve all metrics.
- **POST /api/metrics/**: Create a new metric.
- **GET /api/settings/**: Retrieve user settings.

## Dependencies
See `requirements.txt`.

 