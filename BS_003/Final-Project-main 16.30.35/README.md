# Greenhouse Monitoring API

## Overview
A Django REST API for monitoring greenhouse metrics and managing user settings.

## Features
- User registration, login, and logout
- CRUD operations for greenhouse metrics
- Threshold settings for user-specific alerts
- Token-based authentication

## Endpoints
- `/api/register/` - User registration
- `/api/login/` - User login
- `/api/logout/` - User logout
- `/api/metrics/` - Manage greenhouse metrics
- `/api/settings/` - Manage user-specific settings

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
