# [Unit Conversion Bot](https://t.me/UnitConversionBot)

A [Telegram](https://telegram.org/) bot that converts units (e.g. feet → meters).
Uses [Google App Engine](https://cloud.google.com/appengine/).


## Local Setup
1. Install Python 2.7.
2. [Download](https://cloud.google.com/appengine/docs/standard/python/download) and install the original App Engine SDK for Python.
3. Open _Google App Engine Launcher_.
4. Click _File → Add Existing Application_.
5. Specify the path and click _Add_.
6. `make init`.

To run tests run `make test`.


## Deploy
Get an API key from [Open Exchange Rates](https://openexchangerates.org/signup/free) and save it to `localConfig.py`.
To deploy the bot to Google Cloud click _Deploy_ in _Google App Engine Launcher_.


## License
GNU General Public License v3.0
See [LICENSE.txt](https://github.com/maltsev/UnitConversionBot/blob/master/LICENSE.txt) to see the full text.
