Docker
======

You will need to install Docker first.

Then use Docker to build the image:

.. code-block:: bash

 $ docker build -t mystorefront .


Then you can run Sellor container with the following settings:

.. code-block:: bash

 $ docker run -e SECRET_KEY=<SECRET_KEY> -e DATABASE_URL=<DATABASE_URL> -p 8000:8000 sellor

Please refer to :ref:`settings_configuration` for more environment variable settings.


Heroku
======

Configuration
-------------

Within the repo, git should already be initialized. All you have to do now is add the `heroku` remote with your `app-name`

.. code-block:: console

 $ heroku git:remote -a 'app-name'
 $ heroku buildpacks:add heroku/python
 $ heroku addons:create heroku-postgresql:hobby-dev
 $ heroku addons:create heroku-redis:hobby-dev
 $ heroku addons:create sendgrid:starter
 $ heroku config:set ALLOWED_HOSTS='<your hosts here>'
 $ heroku config:set SECRET_KEY='<your secret key here>'


.. note::
 Heroku's storage is volatile. This means that all instances of your application will have separate disks and will lose all changes made to the local disk each time the application is restarted. The best approach is to use cloud storage such as Amazon S3. See :ref:`amazon-s3` for configuration details.


Deployment
----------

.. code-block:: console

 $ git push heroku master


Preparing the Database
----------------------

.. code-block:: console

 $ heroku run python manage.py migrate


Updating Currency Exchange Rates
--------------------------------

This needs to be run periodically. The best way to achieve this is using Heroku's Scheduler service. Let's add it to our application:

.. code-block:: console

 $ heroku addons:create scheduler

Then log into your Heroku account, find the Heroku Scheduler addon in the active addon list, and have it run the following command on a daily basis:

.. code-block:: console

 $ python manage.py update_exchange_rates --all


Enabling Elasticsearch
----------------------

By default, Sellor uses Postgres as a search backend, but if you want to switch to Elasticsearch, it can be easily achieved using the Bonsai plugin. In order to do that, run the following commands:

.. code-block:: console

 $ heroku addons:create bonsai:sandbox-6 --version=5.4
 $ heroku run python manage.py search_index --create


Storing Files on Amazon S3
==========================

If you're using containers for deployment (including Docker and Heroku) you'll want to avoid storing files in the container's volatile filesystem. This integration allows you to delegate storing such files to `Amazon's S3 service <https://aws.amazon.com/s3/>`_.

Base configuration
------------------

``AWS_ACCESS_KEY_ID``
  Your AWS access key.

``AWS_SECRET_ACCESS_KEY``
  Your AWS secret access key.

Serving media files with a S3 bucket
------------------------------------

If you want to store and serve media files, set the following environment
variable to use S3 as media bucket:

``AWS_MEDIA_BUCKET_NAME``
  The S3 bucket name to use for media files.

If you are intending into using a custom domain for your media S3 bucket,
you can set this environment variable to your custom S3 media domain:

``AWS_MEDIA_CUSTOM_DOMAIN``
  The S3 custom domain to use for the media bucket.


.. note::
 The media files are every data uploaded through the dashboard
 (product images, category images, etc.)


Serving static files with a S3 bucket
-------------------------------------

By default static files (such as CSS and JS files required to display your pages) will be served by the application server.

If you intend to use S3 for your static files as well, set an additional environment variable:

``AWS_STORAGE_BUCKET_NAME``
  The S3 bucket name to use for static files.

If you are intending into using a custom domain for your static S3 bucket,
you can set this environment variable to your custom S3 domain:

``AWS_STATIC_CUSTOM_DOMAIN``
  The S3 custom domain to use for the static bucket.


.. note::
  You will need to configure your S3 bucket to allow cross origin requests for
  some files to be properly served (SVG files, Javascript files, etc.).
  For that, you have to the below instructions in your
  S3 Bucket's permissions tab under the CORS section.

  .. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <AllowedMethod>HEAD</AllowedMethod>
        <MaxAgeSeconds>3000</MaxAgeSeconds>
        <AllowedHeader>*</AllowedHeader>
    </CORSRule>
    </CORSConfiguration>
