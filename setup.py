from setuptools import setup, find_packages
import re

with open('README.md') as fp:
    long_description = fp.read()


def parse_req_line(line):
    line = line.strip()
    if not line or line[0] == '#':
        return None
    return line


def load_requirements(file_name):
    with open(file_name) as fp:
        reqs = filter(None, (parse_req_line(line) for line in fp))
        return list(reqs)


install_requires = load_requirements('requirements.txt')
tests_require = load_requirements('requirements-dev.txt')


setup(
    name="lr2d",
    version='0.1.0',
    packages=find_packages(include=['lr2d', 'lr2d.*']),
    install_requires=install_requires,
    test_suite="tests",
    tests_require=tests_require,
    description="Linear Regression 2-D of housing price against house area",
    long_description=long_description,
    long_description_content_type="text/markdown",
    maintainer="Xander I/O Data",
    maintainer_email="alexander.n.leano@gmail.com",
    url="https://www.xanderiodata.com",
    python_requires=">=3.7, <4",
)
