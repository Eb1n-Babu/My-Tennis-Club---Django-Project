My Tennis Club - Django Project
Introduction
This project, "my_tennis_club," is a Django web application developed following the W3Schools Django tutorial. It demonstrates how to set up a Django project, create an app to manage tennis club members, handle a database with CRUD operations (Create, Read, Update, Delete), and serve static files for styling.
Prerequisites

Python 3.6 or higher
pip (Python package manager)
A command-line tool (e.g., Command Prompt, Terminal)

Step-by-Step Setup
Step 1: Create a Virtual Environment
Create a virtual environment named myworld to isolate dependencies:
python -m venv myworld

Activate the virtual environment:

Windows:myworld\Scripts\activate


macOS/Linux:source myworld/bin/activate



You should see (myworld) in your terminal, indicating the virtual environment is active.
Step 2: Install Django
Install Django in the virtual environment:
pip install django

Step 3: Create the Django Project
Create a Django project named my_tennis_club:
django-admin startproject my_tennis_club

This creates the following structure:
my_tennis_club/
    manage.py
    my_tennis_club/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py

Step 4: Create the Members App
Navigate to the project folder:
cd my_tennis_club

Create a Django app named members:
python manage.py startapp members

Add the members app to INSTALLED_APPS in my_tennis_club/settings.py:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'members.apps.MembersConfig',
]

Step 5: Apply Initial Migrations
Run database migrations to set up the default database:
python manage.py migrate

Step 6: Create the Member Model
In members/models.py, define the Member model:
from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

Create and apply migrations for the Member model:
python manage.py makemigrations
python manage.py migrate

Step 7: Create Templates
Create a templates/ folder in the members/ directory and add the following template files:

all_members.html (to display all members):

<h1>Members</h1>
<ul>
{% for x in mymembers %}
  <li><a href="details/{{ x.id }}">{{ x.firstname }} {{ x.lastname }}</a></li>
{% endfor %}
</ul>
<p><a href="/add/">Add a new member</a></p>


details.html (to show member details):

<h1>{{ mymember.firstname }} {{ mymember.lastname }}</h1>
<p>Back to <a href="/members">Members</a></p>
<p><a href="/update/{{ mymember.id }}">Update member</a></p>
<p><a href="/delete/{{ mymember.id }}">Delete member</a></p>


add.html (to add a new member):

<h1>Add New Member</h1>
<form action="/add/" method="post">
  {% csrf_token %}
  Firstname: <input type="text" name="first" /><br />
  Lastname: <input type="text" name="last" /><br />
  <input type="submit" value="Submit" />
</form>
<p>Back to <a href="/members">Members</a></p>


update.html (to update a member):

<h1>Update Member</h1>
<form action="/update/{{ mymember.id }}" method="post">
  {% csrf_token %}
  Firstname: <input type="text" name="first" value="{{ mymember.firstname }}" /><br />
  Lastname: <input type="text" name="last" value="{{ mymember.lastname }}" /><br />
  <input type="submit" value="Submit" />
</form>
<p>Back to <a href="/members">Members</a></p>

Update my_tennis_club/settings.py to specify the templates directory:
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'members/templates'],
        ...
    }
]

Step 8: Create Views
In members/views.py, define views for handling members:
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {'mymembers': mymembers}
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {'mymember': mymember}
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    if request.method == 'POST':
        new_member = Member(
            firstname=request.POST['first'],
            lastname=request.POST['last']
        )
        new_member.save()
        return HttpResponseRedirect('/members')
    return HttpResponse(template.render({}, request))

def update(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('update.html')
    if request.method == 'POST':
        mymember.firstname = request.POST['first']
        mymember.lastname = request.POST['last']
        mymember.save()
        return HttpResponseRedirect('/members')
    context = {'mymember': mymember}
    return HttpResponse(template.render(context, request))

def delete(request, id):
    mymember = Member.objects.get(id=id)
    mymember.delete()
    return HttpResponseRedirect('/members')

Step 9: Configure URLs
Create members/urls.py:
from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('details/<int:id>', views.details, name='details'),
    path('add/', views.add, name='add'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]

Update my_tennis_club/urls.py to include the members app URLs:
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('members/', include('members.urls')),
    path('admin/', admin.site.urls),
]

Step 10: Add Static Files
Create a static/ folder in the project root (same level as manage.py).
Add a CSS file, e.g., static/my_style.css:
body {
    background-color: lightgrey;
    font-family: Arial;
}

Update my_tennis_club/settings.py to configure static files:
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

Load static files in templates (e.g., in all_members.html):
{% load static %}
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="{% static 'my_style.css' %}">
</head>
<body>
<h1>Members</h1>
<ul>
{% for x in mymembers %}
  <li><a href="details/{{ x.id }}">{{ x.firstname }} {{ x.lastname }}</a></li>
{% endfor %}
</ul>
<p><a href="/add/">Add a new member</a></p>
</body>
</html>

Run the following to collect static files (if deploying):
python manage.py collectstatic

Step 11: Run the Development Server
Start the server:
python manage.py runserver

Access the application at http://127.0.0.1:8000/members/ to view, add, update, or delete members.
Project Details

Purpose: Learn Django basics, including project/app setup, database models, templates, views, URLs, and static file handling.
Main Folder: my_tennis_club/ (project settings and configurations).
App Folder: members/ (handles member-related functionality, including models, views, and templates).
Static Files: Stored in static/ for CSS styling.
Access: Visit http://127.0.0.1:8000/members/ to interact with the application.

Features

Display a list of members with links to their details.
View individual member details.
Add new members via a form.
Update existing member information.
Delete members from the database.
Apply basic CSS styling using static files.

Notes

Ensure the virtual environment is activated before running commands.
If you encounter migration warnings, follow the tutorial to create and apply migrations.
Static files require proper configuration in settings.py and the {% load static %} tag in templates.

Resources

W3Schools Django Tutorial
Django Official Documentation

License
This project is for educational purposes and follows the W3Schools Django tutorial.