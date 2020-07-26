#!/bin/sh

if ['$DATABASE']
then
  echo "pg wait"
  
  while ! nc -z $SQL_HOST $SQL_PORT; do
    sleep 0.1
  done

  echo "pg is up"

fi

python manage.py create_db

exec "$@"
