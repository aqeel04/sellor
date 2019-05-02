release: python manage.py migrate --no-input
web: uwsgi sellor/wsgi/uwsgi.ini
celeryworker: celery worker -A sellor.celeryconf:app --loglevel=info -E
