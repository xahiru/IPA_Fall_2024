# Greenhouse Monitoring System
Superuser id:admin
Password: admin

Setup:
1.Create Virtual Environment
* python -m venv venv
* source venv/bin/activate

2.Install Django
* pip install Django

3.Django Create Project
* django-admin startproject Final_Project

4.Django Create App
* python manage.py startapp api

Project:
5.create serializers for registration and login
6.create views for registration, login and logout
7.create models for greenhouse data and user-setting
migrate with the database
8.create serializers for the models 
9.create views for greenhouse data and user-setting
10.create urls using router