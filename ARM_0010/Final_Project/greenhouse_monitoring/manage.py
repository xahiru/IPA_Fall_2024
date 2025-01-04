#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greenhouse_monitoring.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()





#========================= create user token


from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Get the user object
user = User.objects.get(username='admin')
# Generate or get the token
token, created = Token.objects.get_or_create(user=user)
print(f"Token for {user.username}: {token.key}")
