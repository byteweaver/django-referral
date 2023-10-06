VENV_FOLDER=.venv
POETRY_BIN=poetry
PYTHON_BIN=$(VENV_FOLDER)/bin/python
COVERAGE_BINARY=$(VENV_FOLDER)/bin/coverage
DJANGO_SETTINGS_MODULE='referral.tests.settings'

all: requirements

requirements:
	$(POETRY_BIN) install

test: requirements
	$(POETRY_BIN) run django-admin test --settings=referral.tests.settings

coverage: requirements
	$(COVERAGE_BINARY) erase
	$(COVERAGE_BINARY) run --branch --source=referral $(VENV_FOLDER)/bin/django-admin test --settings=referral.tests.settings
	$(COVERAGE_BINARY) html
