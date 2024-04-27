#!/bin/bash
set -a  # automatically export all variables
[ -f .env ] && . .env
set +a

# Wait for the database to be ready
echo "Waiting for database to be ready..."
python manage.py wait_for_db

# Apply core migrations
echo "Applying core migrations..."
python manage.py migrate admin
python manage.py migrate auth
python manage.py migrate contenttypes
python manage.py migrate sessions

# Make migrations for the 'manager' app
echo "Making migrations for 'fitbox' app..."
python manage.py makemigrations authentication
python manage.py makemigrations customers
python manage.py makemigrations main
python manage.py makemigrations routines

# Apply migrations for the 'manager' app
echo "Migrating"
python manage.py migrate main
python manage.py migrate customers
python manage.py migrate authentication
python manage.py migrate routines

python manage.py create_superuser

echo "Importing"
python manage.py import_days
python manage.py import_levels
python manage.py import_goals
python manage.py import_restrictions
python manage.py import_customer
python manage.py import_muscle_group
python manage.py import_exercises
python manage.py import_blocks
python manage.py import_routines
python manage.py import_routines_days_blocks


python manage.py collectstatic --no-input # this move all static files to server

gunicorn fitbox.wsgi:application --bind 0.0.0.0:8000

echo "Django docker is fully configured successfully."


exec "$@"