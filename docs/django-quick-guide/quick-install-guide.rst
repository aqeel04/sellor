Quick install guide
===================

Before you can use Django, this guide will guide you to a simple, minimal installation that’ll work while you walk through the
introduction.

Install Python
--------------

Being a Python Web framework, Django requires Python. Python includes a lightweight database called SQLite so you won’t need to set up a database just yet.

Get the latest version of Python at https://www.python.org/downloads/ or with your operating system’s package manager.

You can verify that Python is installed by typing python from your shell; you should see something like:

.. code-block:: console

  $ python
  Python 3.x.y
  [GCC 4.x] on linux
  Type "help", "copyright", "credits" or "license" for more information.
  >>>
  
Set up a database
-----------------

This step is only necessary if you’d like to work with a “large” database engine like PostgreSQL, MySQL, or Oracle.
To install such a database, consult the https://docs.djangoproject.com/en/2.1/topics/install/#database-installation.

Install Django
--------------

Installing an official release with pip. This is the recommended way to install Django.

1. Install `pip <https://pip.pypa.io/>`_. The easiest is to use the `standalone pip installer <https://pip.pypa.io/en/latest/installing/>`_. If your distribution already has pip installed, you
might need to update it if it’s outdated. If it’s outdated, you’ll know because installation won’t work.

2. Take a look at `virtualenv <https://virtualenv.pypa.io/>`_. These tools provide isolated Python environments, which are
more practical than installing packages systemwide. They also allow installing packages without administrator
privileges.

After you’ve created and activated a virtual environment, enter the command pip install Django at the
shell prompt. Some think like this

.. code-block:: console

  $ pip install Django
  
Verifying
---------

To verify that Django can be seen by Python, type python from your shell. Then at the Python prompt, try to import
Django:

.. code-block:: console

  $ python
  Python 3.x.y
  [GCC 4.x] on linux
  Type "help", "copyright", "credits" or "license" for more information.
  >>> 
  >>> import django
  >>> print(django.get_version())
  2.1
  
You may have another version of Django installed.

