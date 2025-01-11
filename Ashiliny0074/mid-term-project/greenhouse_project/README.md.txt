# Greenhouse Metrics API

This is a Django REST Framework API for monitoring greenhouse metrics and managing user-specific alert settings.

## Features
- **User Authentication**: Token-based authentication for secure API access.
- **CRUD Operations**:
  - Manage greenhouse metrics (temperature, humidity, soil moisture, and light levels).
  - Configure user-specific alert thresholds.
- **Pagination and Filtering**: Retrieve data in smaller chunks and filter based on specific criteria.
- **Browsable API**: Easily interact with the API using Django REST Framework's browsable interface.

## API Endpoints

### Authentication
- `POST /api-auth/login/`: Login and retrieve an authentication token.
- `POST /api-auth/logout/`: Logout the current user.

### Greenhouse Metrics
- `GET /api/metrics/`: Retrieve all metrics (paginated).
- `POST /api/metrics/`: Add a new metric (authenticated users only).
- `PUT /api/metrics/<id>/`: Update an existing metric (authenticated users only).
- `DELETE /api/metrics/<id>/`: Delete a metric (authenticated users only).

### User Settings
- `GET /api/settings/`: Retrieve user-specific alert thresholds.
- `PUT /api/settings/<id>/`: Update alert thresholds.

## Installation Instructions
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd greenhouse_project

2.	Set Up Virtual Environment:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


3.	Install Dependencies:

pip install -r requirements.txt


4.	Run Migrations:

python manage.py makemigrations
python manage.py migrate


5.	Create a Superuser:

python manage.py createsuperuser


6.	Run the Development Server:

python manage.py runserver


Testing the API
	•	Use tools like Postman or the browsable API (e.g., http://127.0.0.1:8000/api/metrics/) to interact with the API.
	•	Use the authentication token for secure endpoints.