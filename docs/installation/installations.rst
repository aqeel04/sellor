Installation for MacOS
======================

Prerequisites
-------------

Before you are ready to run Sellor you will need additional software installed on your computer.


1. PostgreSQL
^^^^^^^^^^^^^

Sellor needs PostgreSQL version 9.4 or above to work. Get the macOS installer from the `PostgreSQL download page <https://www.postgresql.org/download/macosx/>`_.

Command Line Tools for Xcode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Download and install the latest version of "Command Line Tools (macOS 10.x) for Xcode 9.x" from the `Downloads for Apple Developers page <https://developer.apple.com/download/more/>`_.

Then run:

.. code-block:: console

 $ xcode-select --install


2. Homebrew
^^^^^^^^^^^

Run the following command:

.. code-block:: console

 $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"


3. Python 3
^^^^^^^^^^^

Use Homebrew to install the latest version of Python 3:

.. code-block:: console

 $ brew install python3


4. Git
^^^^^^

Use Homebrew to install Git:

.. code-block:: console

 $ brew install git


5. Gtk+
^^^^^^^

Use Homebrew to install the graphical libraries necessary for PDF creation:

.. code-block:: console

 $ brew install cairo pango gdk-pixbuf libffi


Installation
------------

#. Clone the repository (or use your own fork):

   .. code-block:: console

    $ git clone https://github.com/aqeel04/sellor.git


#. Enter the directory:

   .. code-block:: console

    $ cd sellor/


#. Install all dependencies:

   We strongly recommend `creating a virtual environment <https://docs.python.org/3/tutorial/venv.html>`_ before installing any Python packages.

   .. code-block:: console

    $ pip install -r requirements.txt


#. Set ``SECRET_KEY`` environment variable.

   We try to provide usable default values for all of the settings.
   We've decided not to provide a default for ``SECRET_KEY`` as we fear someone would inevitably ship a project with the default value left in code.

   .. code-block:: console

    $ export SECRET_KEY='<mysecretkey>'

   .. warning::

       Secret key should be a unique string only your team knows.
       Running code with a known ``SECRET_KEY`` defeats many of Django’s security protections, and can lead to privilege escalation and remote code execution vulnerabilities.
       Consult `Django's documentation <https://docs.djangoproject.com/en/1.11/ref/settings/#secret-key>`_ for details.


#. Create a PostgreSQL user:

   Unless configured otherwise the store will use ``sellor`` as both username and password. Remember to give your user the ``SUPERUSER`` privilege so it can create databases and database extensions.

   .. code-block:: console

    $ createuser --superuser --pwprompt sellor

   Enter ``sellor`` when prompted for password.

#. Create a PostgreSQL database:

   Unless configured otherwise the store will use ``sellor`` as the database name.

   .. code-block:: console

    $ createdb sellor

#. Prepare the database:

   .. code-block:: console

    $ python manage.py migrate

   .. warning::

       This command will need to be able to create database extensions. If you get an error related to the ``CREATE EXTENSION`` command please review the notes from the user creation step.

#. Start the development server:

   .. code-block:: console

    $ python manage.py runserver


Installation for Windows
========================

This guide assumes a 64-bit installation of Windows.


Prerequisites
-------------

Before you are ready to run Sellor you will need additional software installed on your computer.


1. Python
^^^^^^^^^

Download the latest **3.7** Windows installer from the `Python download page <https://www.python.org/downloads/>`_ and follow the instructions.

Make sure that "**Add Python 3.7 to PATH**" is checked.


2. PostgreSQL
^^^^^^^^^^^^^

Sellor needs PostgreSQL version 9.4 or above to work. Get the Windows installer from the `project's download page <https://www.postgresql.org/download/windows/>`_.

Make sure you keep track of the password you set for the administration account during installation.


3. GTK+
^^^^^^^

Download the `64-bit Windows installer <https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer>`_.

Make sure that "**Set up PATH environment variable to include GTK+**" is selected.


4. Compilers
^^^^^^^^^^^^

Please download and install the latest version of the `Build Tools for Visual Studio <https://go.microsoft.com/fwlink/?linkid=840931>`_.


Installation
------------

All commands need to be performed in either PowerShell or a Command Shell.

#. Clone the repository (replace the URL with your own fork where needed):

   .. code-block:: cmd

    git clone https://github.com/aqeel04/sellor.git


#. Enter the directory:

   .. code-block:: cmd

    cd sellor/


#. Install all dependencies:

   We strongly recommend `creating a virtual environment <https://docs.python.org/3/tutorial/venv.html>`_ before installing any Python packages.

   .. code-block:: cmd

    python -m pip install -r requirements.txt


#. Set ``SECRET_KEY`` environment variable.

   We try to provide usable default values for all of the settings.
   We've decided not to provide a default for ``SECRET_KEY`` as we fear someone would inevitably ship a project with the default value left in code.

   .. code-block:: cmd

    $env:SECRET_KEY = "<mysecretkey>"

   .. warning::

       Secret key should be a unique string only your team knows.
       Running code with a known ``SECRET_KEY`` defeats many of Django’s security protections, and can lead to privilege escalation and remote code execution vulnerabilities.
       Consult `Django's documentation <https://docs.djangoproject.com/en/1.11/ref/settings/#secret-key>`_ for details.


#. Create a PostgreSQL user:

   Use the **pgAdmin** tool that came with your PostgreSQL installation to create a database user for your store.

   Unless configured otherwise the store will use ``sellor`` as both username and password. Remember to give your user the ``SUPERUSER`` privilege so it can create databases and database extensions.

#. Create a PostgreSQL database

   See `PostgreSQL's createdb command <https://www.postgresql.org/docs/current/static/app-createdb.html>`_ for details.

   .. note::

       Database name is extracted from the ``DATABASE_URL`` environment variable. If absent it defaults to ``sellor``.

#. Prepare the database:

   .. code-block:: cmd

    python manage.py migrate

   .. warning::

       This command will need to be able to create a database and some database extensions. If you get an error related to these make sure you've properly assigned your user ``SUPERUSER`` privileges.

#. Start the development server:

   .. code-block:: cmd

    python manage.py runserver


Installation for Linux
======================


Prerequisites
-------------

Before you are ready to run Sellor you will need additional software installed on your computer.


1. Python 3
^^^^^^^^^^^

Sellor requires Python 3.6 or later. A compatible version comes preinstalled with most current Linux systems. If that is not the case consult your distribution for instructions on how to install Python 3.6 or 3.7.


2. PostgreSQL
^^^^^^^^^^^^^

Sellor needs PostgreSQL version 9.4 or above to work. Use the `PostgreSQL download page <https://www.postgresql.org/download/>`_ to get instructions for your distribution.


3. Gtk+
^^^^^^^

Some features like PDF creation require that additional system libraries are present.

Redhat / Fedora
_______________

.. code-block:: console

 $ sudo yum install redhat-rpm-config python-devel python-pip python-cffi libffi-devel cairo pango gdk-pixbuf2

Debian / Ubuntu
_______________

Debian 9.0 Stretch or newer, Ubuntu 16.04 Xenial or newer:

.. code-block:: console

 $ sudo apt-get install build-essential python3-dev python3-pip python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

Archlinux
_________

.. code-block:: console

 $ sudo pacman -S python-pip cairo pango gdk-pixbuf2 libffi pkg-config

Gentoo
______

.. code-block:: console

 $ emerge pip cairo pango gdk-pixbuf cffi


Installation
------------

#. Clone the repository (or use your own fork):

   .. code-block:: console

    $ sudo git clone https://github.com/aqeel04/sellor.git


#. Enter the directory:

   .. code-block:: console

    $ cd sellor


#. Install all dependencies:

   We strongly recommend `creating a virtual environment <https://docs.python.org/3/tutorial/venv.html>`_ before installing any Python packages.

   .. code-block:: console

    $ sudo pip install -r requirements.txt


#. Set ``SECRET_KEY`` environment variable.

   We try to provide usable default values for all of the settings.
   We've decided not to provide a default for ``SECRET_KEY`` as we fear someone would inevitably ship a project with the default value left in code.

   .. code-block:: console

    $ export SECRET_KEY='<demosecretkey>'
    
    
   .. note::
   
    If your ``SECRET_KEY`` has not set with above command, then navigate to code editor and open up ``sellor/settings.py`` and set ``SECRET_KEY='<demosecretkey>'``.


   .. warning::

       Secret key should be a unique string only your team knows.
       Running code with a known ``SECRET_KEY`` defeats many of Django’s security protections, and can lead to privilege escalation and remote code execution vulnerabilities.
       Consult `Django's documentation <https://docs.djangoproject.com/en/1.11/ref/settings/#secret-key>`_ for details.


#. Create a PostgreSQL user:

   See `PostgreSQL's createuser command <https://www.postgresql.org/docs/current/static/app-createuser.html>`_ for details.

   .. note::

       You need to create the user to use within your project.
       Username and password are extracted from the ``DATABASE_URL`` environmental variable. If absent they both default to ``sellor``.

   .. warning::

       While creating the database Django will need to create some PostgreSQL extensions if not already present in the database. This requires a superuser privilege.

       For local development you can grant your database user the ``SUPERUSER`` privilege. For publicly available systems we recommend using a separate privileged user to perform database migrations.


#. Create a PostgreSQL database

   See `PostgreSQL's createdb command <https://www.postgresql.org/docs/current/static/app-createdb.html>`_ for details.

   .. note::

       Database name is extracted from the ``DATABASE_URL`` environment variable. If absent it defaults to ``sellor``.


#. Prepare the database:

   .. code-block:: console

    $ sudo python manage.py migrate

   .. warning::

       This command will need to be able to create database extensions. If you get an error related to the ``CREATE EXTENSION`` command please review the notes from the user creation step. PostgreSQL extensions that may be required ``hstore``, ``pg_trgm`` and ``btree_gin``.


#. Start the development server:

   .. code-block:: console

    $ sudo python manage.py runserver


Configuration
=============

We are fans of the `12factor <https://12factor.net/>`_ approach and portable code so you can configure most of Sellor using just environment variables.


.. _payment_gateways_configuration:

Payments Gateways
-----------------

``CHECKOUT_PAYMENT_GATEWAYS``
  This contains the list of enabled payment gateways, with the payment friendly name
  to show to the user on the payment selection form.

  For example, to add braintree to the enabled gateways,
  you can do the following:

  .. code-block:: python

    CHECKOUT_PAYMENT_GATEWAYS = {
        DUMMY: pgettext_lazy('Payment method name', 'Dummy gateway'),
        BRAINTREE: pgettext_lazy('Payment method name', 'Brain tree')
    }

  The supported payment providers are:

  - ``DUMMY`` (for tests purposes only!);
  - ``BRAINTREE``;
  - ``RAZORPAY``;
  - ``STRIPE``.


``PAYMENT_GATEWAYS``
    For information on how to configure payment gateways (API keys, miscellaneous information, ...),
    see :ref:`the list of supported payment gateway and their associated environment variables <payment-gateways>`.


Environment variables
---------------------

``ALLOWED_HOSTS``
  Controls `Django's allowed hosts <https://docs.djangoproject.com/en/2.1/ref/settings/#s-allowed-hosts>`_ setting. Defaults to ``localhost``.

  Separate multiple values with comma.

``CACHE_URL`` or ``REDIS_URL``
  The URL of a cache database. Defaults to local process memory.

  Redis is recommended. Heroku's Redis will export this setting automatically.

  **Example:** ``redis://redis.example.com:6379/0``

  .. warning::

      If you plan to use more than one WSGI process (or run more than one server/container) you need to use a shared cache server.
      Otherwise each process will have its own version of each user's session which will result in people being logged out and losing their shopping carts.


``DATABASE_URL``
  Defaults to a local PostgreSQL instance. See :ref:`docker-dev` for how to get a local database running inside a Docker container.

  Most Heroku databases will export this setting automatically.

  **Example:** ``postgres://user:password@psql.example.com/database``

``DEBUG``
  Controls `Django's debug mode <https://docs.djangoproject.com/en/2.1/ref/settings/#s-debug>`_. Defaults to ``True``.

``DEFAULT_FROM_EMAIL``
  Default email address to use for outgoing mail.

``EMAIL_URL``
  The URL of the email gateway. Defaults to printing everything to the console.

  **Example:** ``smtp://user:password@smtp.example.com:465/?ssl=True``

``INTERNAL_IPS``
  Controls `Django's internal IPs <https://docs.djangoproject.com/en/2.1/ref/settings/#s-internal-ips>`_ setting. Defaults to ``127.0.0.1``.

  Separate multiple values with comma.

``SECRET_KEY``
  Controls `Django's secret key <https://docs.djangoproject.com/en/2.1/ref/settings/#s-secret-key>`_ setting.

``SENTRY_DSN``
  Sentry's `Data Source Name <https://docs.sentry.io/quickstart/#about-the-dsn>`_. Disabled by default, allows to enable integration with Sentry (see :ref:`sentry-integration` for details).

``MAX_CART_LINE_QUANTITY``
  Controls maximum number of items in one cart line. Defaults to ``50``.

``STATIC_URL``
  Controls production assets' mount path. Defaults to ``/static/``.

``VATLAYER_ACCESS_KEY``
  Access key to `vatlayer API <https://vatlayer.com/>`_. Enables VAT support within European Union.

  To update the tax rates run the following command at least once per day:

  .. code-block:: console

   $ python manage.py get_vat_rates

``DEFAULT_CURRENCY``
  Controls all prices entered and stored in the store as this single default currency (for more information, see :ref:`money_architecture`).

``DEFAULT_COUNTRY``
  Sets the default country for the store. It controls the default VAT to be shown if required, the default shipping country, etc.

``CREATE_IMAGES_ON_DEMAND``
  Whether or not to create new images on-the-fly (``True`` by default).
  Set this to ``False`` for speedy performance, which is recommended for production.
  Every image should come with a pre-warm to ensure they're
  created and available at the appropriate URL.
  
  
Creating an Administrator Account
=================================

Sellor is a Django application so you can create your master account using the following command:

.. code-block:: console

 $ python manage.py createsuperuser

Follow prompts to provide your email address and password.

You can then start your local server and visit ``http://localhost:8000/dashboard/`` to log into the management interface.

Please note that creating users in this way gives them "superuser" status which means they have all privileges no matter which permissions they have granted.


Debug tools
===========

We have built in support for some of the debug tools.

Django debug toolbar
--------------------

`Django Debug Toolbar <https://github.com/jazzband/django-debug-toolbar>`_ is turned on if Django is running in debug mode.

Silk
----

Silk's presence can be controled via environmental variable

``ENABLE_SILK``
  Controls `django-silk <https://github.com/jazzband/django-silk>`_. Defaults to ``False``

#. Set environment variable.

   .. code-block:: console

    $ export ENABLE_SILK='True'

#. Restart server
