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
