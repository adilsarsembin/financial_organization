#!/bin/sh

DEBUG=${DEBUG}
container_type=${CONTAINER_TYPE};

cd server

if [ $container_type = "CELERY" ]; then
    celery -A celery_app worker --queues=cyber-dynasty-celery

elif [ $container_type = "DJANGO-SERVER" ]; then
    python manage.py collectstatic --noinput --clear
    python manage.py migrate --noinput
    daphne config.server.asgi:application --port 8000 --bind 0.0.0.0
fi;
