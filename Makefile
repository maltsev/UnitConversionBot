test:
	cp tests/test_exchange_rates.json /tmp/unitconversionbot_exchange_rates.json
	pytest tests

serve-local:
	DEBUG=1 chalice local --host 0.0.0.0 --port 8001 --autoreload

lint:
	flake8
	git ls-tree -r --name-only --full-tree HEAD | grep '.py' | xargs pylint --errors-only --output-format=colorized

deploy:
	chalice deploy --stage prod
