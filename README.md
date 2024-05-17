[![Build Status](https://app.travis-ci.com/LeanoA/Python_Package_Project.svg?branch=main)](https://app.travis-ci.com/LeanoA/Python_Package_Project)
[![codecov](https://codecov.io/gh/LeanoA/Python_Package_Project/branch/main/graph/badge.svg?token=KJPUYYVSEA)](https://codecov.io/gh/LeanoA/Python_Package_Project)

# Python Package Project (Example)
## Introduction
This package is a simple implementation of linear regression between two variables: housing price against house area. The package contains the implementation of the algorithm and the unit tests for the algorithm. It is intended to be used as a guide for those who are developing a project in python. 

## Installation
First, clone the repository:
```bash
git clone ...
```
Second, create the environment:
```bash
cd Python_Package_Project
make env
```
Third, activate the environment:
```bash
source vLocalEnv/bin/activate
```
Fourth, install the package:
```bash
cd ..
pip install -e Python_Package_Project
```
where `Python_Package_Project` is the name of the directory where the package is located and it is installed in development mode (flag `-e`). For more information about the installation, please visit: https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/

## Development

### Requirements
The package was developed using `Python 3.9.16` and `make`. The following packages are required to run the code:
* jupyter
* matplotlib
* numpy
* scipy

For more information about the requirements, please visit the `requirements.txt` file.

For the development, the following packages were used:
* pytest
* pytest-mpl
* pytest-mock
* autopep8

For more information about the development requirements, please visit the `requirements-dev.txt` file.

#### Format
This package use autoPEP8 to format the code. For more information about autoPEP8, please visit: https://peps.python.org/pep-0008/

### Development Commands
The following commands are available for the development:
* `make env`: Create a virtual environment, if not exist, and install the requirements. The environment is created in the `vLocalEnv` directory in the root of the project.
* `make dev-env`: Create venv directory if not exist with dev requirements. The environment is created in the `vLocalEnv` directory in the root of the project.
* `make test`: Run tests quickly with the Python in the virtual environment `vLocalEnv`.
* `make clean`: Remove all build, test, coverage and Python artifacts
* `make test-image`: Run tests quickly with the Python in the virtual environment `vLocalEnv` and generate the images for the unit tests.
* `make dist`: Builds source package with sdist. For more information about sdist, please visit: https://packaging.python.org/guides/distributing-packages-using-setuptools/#source-distributions

### Unit Tests without Make

To generate the images base-line for the unit tests, run the following command:
```bash
pytest -k "TestGetPlotForBestFitLine" --mpl-generate-path tests/visualization/baseline
```
This image will be saved in the `tests/visualization/baseline` directory. To run the unit tests and compare the generated images with the base-line images, run the following command:
```bash
pytest -k "TestGetPlotForBestFitLine" --mpl
```
To run the unit tests without make, run the following command:
```bash
pytest --mpl
```

## Badges
To generate the badges travis and codecov, please visit: https://docs.travis-ci.com/user/status-images/ and https://docs.codecov.io/docs/quick-start

## Notes
* If some tests are added and they have the same name but in different files, is necessary to make subpackages of the tests. For more information, please visit: https://docs.pytest.org/en/6.2.x/goodpractices.html#tests-outside-application-code
