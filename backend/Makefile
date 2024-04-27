include .env

prepare:
	make delete_migrations
	make migrations
	make migrate
	make create_superuser
#Si se rompe esto, sacar las foreing keys de la tabla customers a routines, hacer una primer pasada y despues habilitarlas

delete_migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
	find . -path "./db.sqlite3" -delete

run:
	make migrate
	pipenv run python manage.py runserver

migrate:
	pipenv run python manage.py migrate
	pipenv run python manage.py migrate main
	pipenv run python manage.py migrate customers
	pipenv run python manage.py migrate authentication
	pipenv run python manage.py migrate routines

migrations:
	pipenv run python manage.py makemigrations authentication
	pipenv run python manage.py makemigrations customers
	pipenv run python manage.py makemigrations main
	pipenv run python manage.py makemigrations routines

coverage:
	@pipenv run coverage html
	@echo
	@echo "Generating coverage report..."
	@printf '**** Code Coverage Total: \033[30;48;5;82m  '
	@echo -n $(shell pipenv run coverage report | grep TOTAL | awk '{print $$4}')
	@printf '  \033[0m **** '
	@echo

shell:
	pipenv run python manage.py shell

import_all:
	pipenv run python manage.py import_days
	pipenv run python manage.py import_levels
	pipenv run python manage.py import_goals
	pipenv run python manage.py import_restrictions
	pipenv run python manage.py import_customer
	pipenv run python manage.py import_muscle_group
	pipenv run python manage.py import_exercises
	pipenv run python manage.py import_blocks
	pipenv run python manage.py import_routines
	pipenv run python manage.py import_routines_days_blocks

import_data:
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


test:
	pipenv run pytest -s --durations=10 --create-db

create_superuser:
	pipenv run python manage.py create_superuser

create_superuser_by_cmd:
	pipenv run python manage.py createsuperuser --noinput --email=${DJANGO_SUPERUSER_EMAIL} --first_name=${DJANGO_SUPERUSER_FIRST_NAME}