# [Unit Conversion Bot](https://t.me/UnitConversionBot) [![Build Status](https://travis-ci.org/maltsev/UnitConversionBot.svg?branch=master)](https://travis-ci.org/maltsev/UnitConversionBot)

A [Telegram](https://telegram.org/) bot that converts units (e.g. feet → meters).
Uses [AWS Lambda](https://aws.amazon.com/lambda/).


## Local Setup
1. Install Python 3 and [pipenv](https://pipenv.pypa.io/en/latest/).
1. Run `pipenv install --dev`.
2. Run `pipenv run make serve-local` to run it locally.

To run tests run `pipenv run make test`.


## Deploy
Copy `.chalice/config.example.json` to `.chalice/config.json`.
Insert an API key from [Open Exchange Rates](https://openexchangerates.org/signup/free) and a S3 bucket name to the config file.


## License
GNU General Public License v3.0
See [LICENSE.txt](https://github.com/maltsev/UnitConversionBot/blob/master/LICENSE.txt) to see the full text.
