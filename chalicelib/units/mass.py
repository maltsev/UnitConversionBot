# Main symbol — µ (U+00B5), second — μ (U+03BC)
NANOGRAM = (1e-9, ['ng', 'nanogram', 'nanograms', 'nanogramme', 'nanogrammes'], 'MICROGRAM')
MICROGRAM = (1e-6, ['µg', 'microgram', 'micrograms', 'microgramme', 'microgrammes', 'μg', 'ug'], 'MILLIGRAM')
MILLIGRAM = (0.001, ['mg', 'milligram', 'milligrams', 'milligramme', 'milligrammes'], 'GRAM')
GRAM = (1, ['g', 'gram', 'grams', 'gramme', 'grammes'], 'MILLIGRAM')
KILOGRAM = (1000, ['kg', 'kilogram', 'kilograms', 'kilogramme', 'kilogrammes'], 'POUND')
TONNE = (1e6, ['t', 'tonne', 'tonnes', 'megagramm', 'megagramms', 'megagramme', 'megamgrammes', 'ton'], 'KILOGRAM')

POUND = (453.59237, ['lb', 'pound', 'pounds', 'lbm', 'lbs'], 'GRAM')
OUNCE = (POUND[0] / 16, ['oz', 'ounce', 'ounces'], 'GRAM')

TROY_OUNCE = (OUNCE[0] * (192.0/175), ['ozt', 'troy ounce', 'troy ounces'], 'GRAM')
TROY_POUND = (TROY_OUNCE[0] * 12, ['tlb', 'troy pound', 'troy pounds'], 'GRAM')
TROY_GRAIN = (TROY_POUND[0] / 5760, ['gr', 'troy grain', 'troy grains', 'grain', 'grains'], 'MILLIGRAM')
PENNYWEIGHT = (TROY_GRAIN[0] * 24, ['dwt', 'pennyweight'], 'GRAM')

_BASE = 'GRAM'
