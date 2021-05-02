from tests.functional import check


def test_convertWithoutCommand():
    check(
        '544.311 g',
        text='1.2 LB TO Gram'
    )


def test_convertWithoutCommandAndWithBotName():
    check(
        '3.6 km/h',
        text='@UnitConversionBot 1 m/s to km/h'
    )


def test_convertCurrencies():
    check(
        '2.179 CZK',
        text='10.5 Icelandic Króna to Kč',
    )
    check(
        '3.913 €',
        text='1 mBTC to €',
    )


def test_convert(caplog):
    check(
        '0.093 m²',
        text='/convert 1 ft² to m²',
    )


def test_emptyConvertExpression():
    check(
        'Please type something like "/convert 100 ft to m"',
        text='/convert ',
    )


def test_convertWithBotName():
    check(
        '24 h',
        text='/convert@UnitConversionBot 1 day to hours'
    )


def test_convertMultilineExpression():
    check(
        '3,600 km/h',
        text='1000 m/s to km/h\n10 fl.oz to litres',
    )


def test_convertWithoutToUnit():
    check(
        '30.48 m',
        text='/convert 100 ft to',
    )


def test_invalidExpression(caplog):
    check(
        "Sorry, I'm just a stupid bot :-( I don't know what does 'фут' mean. But my master probably does. I'd ask him to teach me.",
        text='1 фут в метры',
    )


def test_convertIncompatibleUnitCategories(caplog):
    check(
        "Sorry, I can't convert foot to gram (at least in this universe).",
        text='1 ft to g',
    )


def test_convertNotExistsFromUnit(caplog):
    check(
        "Sorry, I'm just a stupid bot :-( I don't know what does 'blablagram²' mean. But my master probably does. I'd ask him to teach me.",
        text='1 blablagram² to gram',
    )


def test_convertNotExistsUnits():
    check(
        "Sorry, I'm just a stupid bot :-( I don't know what does 'blablagram' mean. But my master probably does. I'd ask him to teach me.",
        text='1.2 blablagram to wtfgram',
    )


def test_convertInvalidUnitValue(caplog):
    check(
        "Sorry, I don't understand the number 'one'. Please type it in a more ordinary way, like 100 or 12.5",
        text='one ft to m',
    )


def test_convertHugeNumber(caplog):
    check(
        "Sorry, I can't convert such big numbers.",
        text='99999999999.999 km to m',
    )
    check(
        "99,999,999,999,990 m",
        text='99999999999.99 km to m',
    )
