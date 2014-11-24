VENV_FOLDER=env
PIP_BIN=$(VENV_FOLDER)/bin/pip
PYTHON_BIN=$(VENV_FOLDER)/bin/python

all: environment requirements

environment:
	test -d "$(VENV_FOLDER)" || virtualenv --no-site-packages $(VENV_FOLDER)

requirements:
	$(PIP_BIN) install -r requirements.txt

test:
	$(PYTHON_BIN) referral/tests/runtests.py

