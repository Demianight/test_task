run:
	python3 manage.py runserver

superuser:
	python3 manage.py createsuperuser

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

venv:
	python3 -m venv venv

docker: migrate
	python3 manage.py collectstatic	--no-input
	docker build . -t test_task
	docker run -p 8000:8000 test_task