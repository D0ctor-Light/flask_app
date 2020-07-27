#!/bin/sh

if ['$DATABASE']
then
  echo "pg wait"
  
  while ! nc -z $SQL_HOST $SQL_PORT; do
    sleep 0.1
  done

  echo "pg is up"

fi

if [ "$FLASK_ENV" = "development" ]
then
    echo "Creating the database"
    python manage.py create_db
    echo "created"
fi

exec "$@"
