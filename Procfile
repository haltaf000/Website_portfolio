web: python manage.py collectstatic --noinput && python manage.py migrate && gunicorn personal_web.wsgi:application --bind 0.0.0.0:$PORT --log-file -
