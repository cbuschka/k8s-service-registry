build:	__cond-setup
	docker build --tag k8s-registry:latest .

run:	__cond-setup
	source .venv/bin/activate && PYTHONPATH=. python3 -m k8s_registry

__cond-setup:
	if [ ! -d ".venv/" ]; then make setup; fi

setup:
	python3 -m virtualenv --python=python3.7 .venv/
	source .venv/bin/activate && pip3 install -r requirements.txt
