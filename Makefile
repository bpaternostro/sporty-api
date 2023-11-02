prepare:
	make migrations
	make migrate
#Si se rompe esto, sacar las foreing keys de la tabla customers a routines, hacer una primer pasada y despues habilitarlas

run:
	make migrate
	pipenv run python manage.py runserver

migrate:
	pipenv run python manage.py migrate
	pipenv run python manage.py migrate main
	pipenv run python manage.py migrate customers
	pipenv run python manage.py migrate routines
	pipenv run python manage.py migrate authentication

migrations:
	pipenv run python manage.py makemigrations main
	pipenv run python manage.py makemigrations customers
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
	pipenv run python manage.py import_lang
	pipenv run python manage.py import_status
	pipenv run python manage.py import_muscle_group_type
	pipenv run python manage.py import_days
	pipenv run python manage.py import_goals
	pipenv run python manage.py import_levels
	pipenv run python manage.py import_training_method
	pipenv run python manage.py import_restrictions
	pipenv run python manage.py import_routine_types
	pipenv run python manage.py import_systems
	pipenv run python manage.py import_block_types
	pipenv run python manage.py import_customer
	pipenv run python manage.py import_muscle_group
	pipenv run python manage.py import_exercises
	pipenv run python manage.py import_blocks
	pipenv run python manage.py import_routines
	pipenv run python manage.py import_routines_days_blocks


test:
	pipenv run pytest -s --durations=10 --create-db

