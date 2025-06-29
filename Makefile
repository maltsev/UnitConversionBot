test:
	cp tests/test_exchange_rates.json /tmp/unitconversionbot_exchange_rates.json
	pytest tests -v

serve-local:
	DEBUG=1 chalice local --host 0.0.0.0 --port 8001 --autoreload

lint:
	ruff check .
	black --check .

prettify:
	ruff format .
	black .

deploy:
	chalice deploy --stage prod
