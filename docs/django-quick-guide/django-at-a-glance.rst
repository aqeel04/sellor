Django at a glance
==================

Because Django was developed in a fast-paced newsroom environment, it was designed to make common Webdevelopment tasks fast and easy. Here’s an informal overview of how to write a database-driven Web app with Django.

The goal of this document is to give you enough technical specifics to understand how Django works, but this isn’t
intended to be a tutorial or reference – but we’ve got both! When you’re ready to start a project, you can :ref:`start with the
tutorial <building-your-first-django-app,-part-1>`.

Design your model
-----------------

Although you can use Django without a database, it comes with an object-relational mapper in which you describe
your database layout in Python code.

The data-model syntax offers many rich ways of representing your models – so far, it’s been solving many years’
worth of database-schema problems. Here’s a quick example: mysite/news/models.py

.. code-block:: python
  
  from django.db import models

  class Reporter(models.Model):
      full_name = models.CharField(max_length=70)

      def __str__(self):
          return self.full_name

  class Article(models.Model):
      pub_date = models.DateField()
      headline = models.CharField(max_length=200)
      content = models.TextField()
      reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

      def __str__(self):
          return self.headline

Next, run the Django command-line utility to create the database tables automatically:

.. code-block:: console
  
  $ python manage.py migrate

The migrate command looks at all your available models and creates tables in your database for whichever tables
don’t already exist, as well as optionally providing much richer schema control.

A dynamic admin interface
-------------------------

Once your models are defined, Django can automatically create a professional, production ready administrative interface – a website that lets authenticated users add, change and delete objects. It’s as easy as registering your model in
the admin site: mysite/news/admin.py

.. code-block:: python

  from django.contrib import admin
  from . import models

  admin.site.register(models.Article)

Design your URLs
----------------

A clean, elegant URL scheme is an important detail in a high-quality Web application. Django encourages beautiful
URL design and doesn’t put any cruft in URLs, like .php or .asp.

To design URLs for an app, you create a Python module called a URLconf . A table of contents for your app, it contains
a simple mapping between URL patterns and Python callback functions. URLconfs also serve to decouple URLs from
Python code.

Here’s URLconf file: mysite/news/urls.py

.. code-block:: python

  from django.urls import path
  from . import views

  urlpatterns = [
      path('articles/<int:year>/', views.year_archive),
      path('articles/<int:year>/<int:month>/', views.month_archive),
      path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
  ]

The code above maps URL paths to Python callback functions (“views”). The path strings use parameter tags to
“capture” values from the URLs. When a user requests a page, Django runs through each path, in order, and stops at
the first one that matches the requested URL. (If none of them matches, Django calls a special-case 404 view.) This is
blazingly fast, because the paths are compiled into regular expressions at load time.

Once one of the URL patterns matches, Django calls the given view, which is a Python function. Each view gets
passed a request object – which contains request metadata – and the values captured in the pattern.

Write your views
----------------

Each view is responsible for doing one of two things: Returning an HttpResponse object containing the content
for the requested page, or raising an exception such as Http404. The rest is up to you.

Generally, a view retrieves data according to the parameters, loads a template and renders the template with the
retrieved data. Here’s an example view: mysite/news/views.py

.. code-block:: python
 
  from django.shortcuts import render
  from .models import Article

  def year_archive(request, year):
      a_list = Article.objects.filter(pub_date__year=year)
      context = {'year': year, 'article_list': a_list}
      return render(request, 'news/year_archive.html', context)

This example uses Django’s template system, which has several powerful features but strives to stay simple enough
for non-programmers to use.

Design your templates
---------------------

The code above loads the news/year_archive.html template.

Django has a template search path, which allows you to minimize redundancy among templates. In your Django
settings, you specify a list of directories to check for templates with DIRS. If a template doesn’t exist in the first
directory, it checks the second, and so on.

Let’s say the news/year_archive.html template was found. Here’s what that might look like: mysite/news/templates/news/year_archive.html

.. code-block:: html

  {% extends "base.html" %}
  {% block title %}Articles for {{ year }}{% endblock %}
  {% block content %}
    <h1>Articles for {{ year }}</h1>
    {% for article in article_list %}
       <p>{{ article.headline }}</p>
       <p>By {{ article.reporter.full_name }}</p>
       <p>Published {{ article.pub_date|date:"F j, Y" }}</p>
    {% endfor %}
  {% endblock %}

Variables are surrounded by double-curly braces. {{ article.headline }} means “Output the value of the
article’s headline attribute.” But dots aren’t used only for attribute lookup. They also can do dictionary-key lookup,
index lookup and function calls.

Finally, Django uses the concept of “template inheritance”. That’s what the {% extends "base.html" %}
does. It means “First load the template called ‘base’, which has defined a bunch of blocks, and fill the blocks with
the following blocks.” In short, that lets you dramatically cut down on redundancy in templates: each template has to
define only what’s unique to that template.

Here’s what the “base.html” template, including the use of static files, might look like: mysite/templates/base.html

.. code-block:: html

  {% load static %}
  <html>
    <head>
      <title>{% block title %}{% endblock %}</title>
    </head>
    <body>
      <img src="{% static "images/sitelogo.png" %}" alt="Logo">
      {% block content %}{% endblock %}
    </body>
  </html>

Simplistically, it defines the look-and-feel of the site (with the site’s logo), and provides “holes” for child templates to
fill. This makes a site redesign as easy as changing a single file – the base template.

It also lets you create multiple versions of a site, with different base templates, while reusing child templates. Django’s
creators have used this technique to create strikingly different mobile versions of sites – simply by creating a new base
template.

Note that you don’t have to use Django’s template system if you prefer another system. While Django’s template
system is particularly well-integrated with Django’s model layer, nothing forces you to use it. For that matter, you
don’t have to use Django’s database API, either. You can use another database abstraction layer, you can read XML
files, you can read files off disk, or anything you want. Each piece of Django – models, views, templates – is decoupled
from the next.
