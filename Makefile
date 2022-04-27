all: deps lint test

deps:
	@python3 -m pip install --upgrade pip && pip3 install -r requirements-dev.txt

black:
	@black --line-length 120 uk_modulus_check tests

isort:
	@isort --line-length 120 --use-parentheses --multi-line 3 --combine-as --trailing-comma uk_modulus_check tests

mypy:
	@mypy --strict --ignore-missing-imports uk_modulus_check

flake8:
	@flake8 --max-line-length 120 --ignore C901,C812,E203 --extend-ignore W503 uk_modulus_check tests

lint: black isort flake8 mypy

test:
	@python3 -m pytest -vv --rootdir tests .

pyenv:
	echo uk-modulus-check > .python-version && pyenv install -s 3.10.3 && pyenv virtualenv -f 3.10.3 uk-modulus-check
