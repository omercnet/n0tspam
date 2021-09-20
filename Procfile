web: daphne asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: celery -A n0temail worker -B