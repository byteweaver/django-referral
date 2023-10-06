VENV_FOLDER=env
PIP_BIN=$(VENV_FOLDER)/bin/pip
PYTHON_BIN=$(VENV_FOLDER)/bin/python
COVERAGE_BINARY=$(VENV_FOLDER)/bin/coverage
DJANGO_SETTINGS_MODULE='referral.tests.settings'

all: environment requirements

environment:
	test -d "$(VENV_FOLDER)" || virtualenv --no-site-packages $(VENV_FOLDER)

requirements:
	$(PIP_BIN) install -r requirements.txt

test: requirements
	$(PYTHON_BINARY) env/bin/django-admin test --settings=referral.tests.settings

coverage: requirements
		$(COVERAGE_BINARY) erase
		$(COVERAGE_BINARY) run --branch --source=referral env/bin/django-admin test --settings=referral.tests.settings
		$(COVERAGE_BINARY) html
