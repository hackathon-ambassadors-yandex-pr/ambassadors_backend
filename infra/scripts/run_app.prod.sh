python manage.py migrate --no-input;
python manage.py loaddata data.json;
gunicorn octopus.wsgi:application --bind 0:8008;
