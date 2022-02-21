ACTIVATE := ./.venv/bin/activate

ifeq '$(findstring ;,$(PATH))' ';'
	ACTIVATE := .\.venv\Scripts\activate
endif

setup:
		python -m venv .venv
		$(ACTIVATE)

install:
		pip install --upgrade pip &&\
		pip install -r requirements_dev.txt

local:
		mypy -m {{cookiecutter.package_slug}}
		flake8 {{cookiecutter.package_slug}} tests
		pytest tests

ci:
		tox