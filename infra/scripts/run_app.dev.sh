python manage.py migrate --no-input
python manage.py createsuperuser --no-input
python manage.py loaddata data.json test_data.json
gunicorn config.wsgi:application --bind 0:8008
