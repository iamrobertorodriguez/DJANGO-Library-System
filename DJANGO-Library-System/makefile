# Makefile para Django

# Comando para iniciar la aplicación Django
run:
	python manage.py migrate && \
	python manage.py collectstatic --no-input && \
	python manage.py runserver 0.0.0.0:8010

# Comando para aplicar las migraciones
migrate:
	python manage.py migrate

# Comando para crear una nueva migración
makemigrations:
	python manage.py makemigrations