#First we need to install python, pip & virtual environment in our local system.

    check version: python --version 
                   pip --version

Step:1 
created a virtual environment for the project:

    windows: python -m venv env

    activate the virtual environment (ALWAYS ACTIVATE THE VIRTUAL ENVIRONMENT BEFORE START WORKING)
    windows: (evn)\Scripts\activate.bat

Step:2
Install Django:

    after active virtual environment in terminal you get a line look like this (env)
    
    \RG0042\Final_Project\env\Scripts>
    After thst Run this commend
     
    windows: python -m pip install Django
    check version : django-admin --version

Step:3
create a django project:

    windows: django-admin startproject <..name..>
    
    greenhouse_project
    run the live server:
     windows: python manage.py runserver

Step:4
Install all Dependencies:
    first we need to add requirements.txt file & write all dependencies in txt file.

    installation commend:
    windows: pip install -r requirements.txt

Step:5
Django Create App:

    windows: python manage.py startapp <...name...>

Step:5
Migrate: 

    python manage.py makemigrations
    python manage.py migrate

Step:6
Now We will add File & Code What we need to complete this project step ny step.

Step:7
Django Admin - Create User

    py manage.py createsuperuser

