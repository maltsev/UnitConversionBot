init:
	@if [ ! -f localConfig.py ]; then cp localConfig.example.py localConfig.py; fi

test:
	python tests/run.py
