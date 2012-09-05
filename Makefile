VENV_FOLDER=env
PIP_BIN=$(VENV_FOLDER)/bin/pip

all: environment reqirements

environment:
	test -d "$(VENV_FOLDER)" || virtualenv --no-site-packages $(VENV_FOLDER)

reqirements:
	$(PIP_BIN) install -r requirements.txt

