# [Unit Conversion Bot](https://t.me/UnitConversionBot) ![Build status](https://github.com/maltsev/UnitConversionBot/actions/workflows/ci.yml/badge.svg)

A [Telegram](https://telegram.org/) bot that converts units (e.g. feet → meters).
Uses [AWS Lambda](https://aws.amazon.com/lambda/).


## Local Setup
1. Install [uv](https://docs.astral.sh/uv/).
2. Run `uv run make serve-local` to run it locally.

To run tests run `uv run make test`.


## Deploy
Copy `.chalice/config.example.json` to `.chalice/config.json`.
Insert an API key from [Open Exchange Rates](https://openexchangerates.org/signup/free) and a S3 bucket name to the config file.


## License
GNU General Public License v3.0
See [LICENSE.txt](https://github.com/maltsev/UnitConversionBot/blob/master/LICENSE.txt) to see the full text.
