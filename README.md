CRUD for Notes:
===============

This project's goal is to probe make a CRUD app with minimal code, 
supporting in the use of Django facilities.

It's a probe to build requirements.txt and deployment too.


Base:
-----

This project is based on https://www.uno-de-piera.com/crud-con-django-y-mysql
with some changes:
- Use of mysql-connector-python-rf package (seems more updated than 
  default mysql connector package)
- Css rules added
- Remove url field from model Post and add publish date field; thus a date 
  widget is used
- Static files definitions according to Django docs
- Personalize application definition, divide it into two sections


Status:
-------

Deploying in pythonanywere


Pending:
--------

- Some changes to personalize this project
- Deployment in pythonanywere
