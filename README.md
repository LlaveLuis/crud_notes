CRUD for Notes:
===============

This project's goal is to probe make a CRUD app with minimal code, 
supporting in the use of Django facilities. In addition, basic user login
is included, and some functionalities using javascript code.

It's a probe to build requirements.txt and deployment too.


Characteristics:
----------------

- User login and logout functionalities. Include Remember me function.
- Password stored as a hash.
- Use of bootstrap facilities and jquery-messagebox plugin, as tools for show
  a message with credentials for existing users.
- Menu shows user name.
- List of saved posts, which can be updated or deleted. Posts are showed in 
  publication date order.
- Normal users can view only own posts, admin users can view all posts and, 
  in addition, filter them by user.
- Use of SelectDateWidget in New Post form.
- Form to update post is placed in modal window. Data load throught ajax call.
- Static files definitions according to Django docs.
- Use of mysql-connector-python-rf package (seems more updated than 
  default mysql connector package).


This project's seeder idea is on https://www.uno-de-piera.com/crud-con-django-y-mysql,
where a simple CRUD app for notes is proposed, including only View, Create, Update and 
Delete posts functionalities.

Some css rules and js/jquery code was added; and a better overall behaviour has been 
achieved.


URL for this Project in Deployment:
-----------------------------------

[Crud notes in pythonanywhere](http://llaveluis.pythonanywhere.com)
