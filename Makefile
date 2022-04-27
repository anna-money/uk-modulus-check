.EXPORT_ALL_VARIABLES:
DIRECTORY = uk_modulus_check

all: deps lint test

deps:
	@python3 -m pip install --upgrade pip && pip3 install -r requirements-dev.txt

lint: black isort flake8 mypy

mypy:
	mypy $(DIRECTORY)
	mypy tests

flake8:
	flake8 $(DIRECTORY)
	flake8 tests
	flake8 setup.py

black:
ifeq ($(MODE), ci)
	black $(DIRECTORY) --check
	black tests --check
	black setup.py --check
else
	black $(DIRECTORY)
	black tests
	black setup.py
endif

isort:
ifeq ($(MODE), ci)
	isort $(DIRECTORY) -c
	isort tests -c
else
	isort $(DIRECTORY)
	isort tests
	isort setup.py
endif

test:
	@python3 -m pytest -vv --rootdir tests .

pyenv:
	echo uk-modulus-check > .python-version && pyenv install -s 3.10.3 && pyenv virtualenv -f 3.10.3 uk-modulus-check
