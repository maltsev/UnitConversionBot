import json
from model import Rates

exchangeRates = """

"""

Rates(content=json.loads(exchangeRates)).put()
