web: gunicorn portfolio_web.wsgi --log-file - 
web: python manage.py migrate && gunicorn portfolio_web.wsgi