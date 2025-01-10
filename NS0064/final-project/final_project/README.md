*****superuser id:admin, pass:admin****

***installed python,pip and virtual environment***

# created a virtual environment
    python -m venv .venv
# activate the virtual environment
    myenv\Scripts\activate
# install django, djangorestframework, django-cors-headers 
    pip install django djangorestframework djoser django-cors-headers
# create a project
    django-admin startproject final_project
# create an app
    python manage.py startapp api
# run the live server 
    python manage.py runserver

***coding steps***
1. create serializer for registration and login
2. create views for registration, login and logout
3. create models for greenhouse data and user-setting
    migrate into the database
4. create serializers for the models
5. create views for greenhouse data and user-setting
6. create urls using router
7. create superuser 