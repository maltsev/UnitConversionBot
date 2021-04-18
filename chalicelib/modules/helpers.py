import logging
import os
import urllib
import json

logger = logging.getLogger()


def generateCompositeNames(firstUnitNames, lastUnitNames, shortName=None):
    """Generate composite names using "per" and "/"
    (e.g., km/h, kilometers per hour)
    """
    if not shortName:
        shortName = firstUnitNames[0] + '/' + lastUnitNames[0]  # e.g., kg/m³

    fullName = firstUnitNames[1] + ' per ' + lastUnitNames[1]  # e.g., kilogram per cubic meter

    names = [
        shortName,
        fullName,
    ]

    for firstUnitName in firstUnitNames:
        for lastUnitName in lastUnitNames:
            newFullName = firstUnitName + ' per ' + lastUnitName

            if newFullName not in names:
                names.append(newFullName)

            newShortName = firstUnitName + '/' + lastUnitName
            if ' ' not in newShortName and newShortName not in names:
                names.append(newShortName)

    return names


EXCHANGE_RATES_FILE_NAME = 'exchange_rates.json'


def fetchExchangeRates():
    if fetchExchangeRates.cache:
        return fetchExchangeRates.cache

    cache_path = '/tmp/unitconversionbot_exchange_rates.json'
    exchange_rates_str = ''
    if os.path.isfile(cache_path):
        with open(cache_path, 'r') as f:
            exchange_rates_str = f.read().strip()

    if not exchange_rates_str:
        S3_BUCKET = os.environ['S3_BUCKET']
        S3_BUCKET_REGION = os.environ['S3_BUCKET_REGION']
        url = f'https://{S3_BUCKET}.s3.{S3_BUCKET_REGION}.amazonaws.com/{EXCHANGE_RATES_FILE_NAME}'
        response = urllib.request.urlopen(url)
        exchange_rates_str = response.read().decode('utf-8')
        with open(cache_path, 'w') as f:
            f.write(exchange_rates_str)

    fetchExchangeRates.cache = json.loads(exchange_rates_str)['rates']
    return fetchExchangeRates.cache


fetchExchangeRates.cache = None
