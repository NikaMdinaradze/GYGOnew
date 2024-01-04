requirements:
	@echo "Installing requirements"
	pip install -r requirements.txt

migrations:
	@echo "Making Migration files"
	python manage.py makemigrations

migrate:
	@echo "Running Migrations Docker"
	python manage.py migrate

tests:
	@echo "running tests docker"
	python manage.py test
