all:
	$(error please pick a target)

env:
	# Create venv directory if not exist
	test -d vLocalEnv || virtualenv vLocalEnv
	./vLocalEnv/bin/python -m pip install -r requirements.txt

dev-env: env
	./vLocalEnv/bin/python -m pip install -r requirements-dev.txt

package:
	python setup.py sdist

test:
	./vLocalEnv/bin/python -m pytest \
		--doctest-modules \
	    --disable-warnings \
	    --verbose \
	    lr2d tests --mpl

clean:
	rm -rf dist lr2d/lr2d.egg-info
