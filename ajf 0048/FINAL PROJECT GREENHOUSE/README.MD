# Greenhouse Monitoring System

A Django REST API for monitoring greenhouse environmental conditions.

## Features
- Real-time greenhouse metrics monitoring
- User authentication and authorization
- Data visualization dashboard
- API endpoints for temperature, humidity, soil moisture
- Filtering and pagination
- Admin interface for data management

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>

## Installation
1. Clone the repository: 'git clone <repository-url>'
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment: 
On Windows:`venv\Scripts\activate`
On MacOS: 'source venv/bin/activate'
4. Install requirements: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create superuser: `python manage.py createsuperuser`
7. Run server: `python manage.py runserver`

## API Endpoints
- GET /api/metrics/ - List all metrics
- POST /api/metrics/ - Create new measurement
- GET /api/metrics/{id}/ - Retrieve specific measurement
- PUT /api/metrics/{id}/ - Update measurement
- DELETE /api/metrics/{id}/ - Delete measurement

## Authentication
Uses Token Authentication. Generate token using:

python manage.py drf_create_token username

# Project Title
GREENHOUSE

## Admin Access

To access the Django admin interface, use the following credentials:

- **Username**: `Xahiru`
- **Password**: `IPA12345`

### Accessing the Admin Interface

1. Navigate to the admin interface at: [http://localhost:8000/admin/](http://localhost:8000/admin/)
2. Enter the provided username and password.
3. Click the "Log in" button.

### Important Notes

- Make sure the Django server is running. You can start it with the following command:

  python manage.py runserver

### Dependencies
Django
Django REST Framework
drf-yasg (for Swagger documentation)

### Usage Examples
List All Metrics
Request:
curl -X GET http://localhost:8000/api/metrics/ -H "Authorization: Token your_token_here"

Response:
[
  {
    "id": 1,
    "temperature": 25.5,
    "humidity": 65,
  },
]

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Contact
For any questions or support, please contact [kedifrances@gmail.com].
