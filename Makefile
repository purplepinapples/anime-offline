reinstall: clean uninstall install

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	rm -fr *.egg-info/

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

install:
	python3 setup.py install

installv: # verbose
	python3 setup.py -v install

uninstall:
	pip3 uninstall -y animeoffline

test:
	python3 -m pytest --tb=native
