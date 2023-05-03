.DEFAULT_GOAL := help


define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

all:
	$(error please pick a target)

env: ## Create venv directory if not exist
	test -d vLocalEnv || virtualenv vLocalEnv
	./vLocalEnv/bin/python -m pip install -r requirements.txt

dev-env: env ## Create venv directory if not exist with dev requirements
	./vLocalEnv/bin/python -m pip install -r requirements-dev.txt
	
clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -fr .pytest_cache

test: ## run tests quickly with the Python in the virtual environment vLocalEnv
	./vLocalEnv/bin/python -m pytest \
		--doctest-modules \
	    --disable-warnings \
	    --verbose \
	    lr2d tests --mpl

test-image: ## generate the images base-line for the image unit tests
	./vLocalEnv/bin/python -m pytest \
	-k "TestGetPlotForBestFitLine" --mpl-generate-path tests/visualization/baseline



# Descomment this if you want to run the tests in all python versions
# test-all: ## run tests on every Python version with tox
# 	tox

# Descomment this if you want to upload the package to pypi
# release: dist ## package and upload a release
# 	twine upload dist/*

dist: clean ## builds source package
	python3 setup.py sdist
	ls -l dist

# Descomment this if you want the package to be installed in your local python
# install: clean ## install the package to the active Python's site-packages
# 	python3 setup.py install