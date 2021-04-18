from tests.functional import check_inline


def test_inlineConvert():
    check_inline(
        '100,000 dm²',
        '1,000 m² = 100,000 dm²',
        query='1000 m² to dm2',
    )


def test_inlineEmpty():
    check_inline(
        '10 ft to m',
        '10 ft = 3.048 m',
        description='Please type a convert expression (e.g., "10 ft to m").',
        query='',
    )


def test_inlineConvertWithoutToUnit():
    check_inline(
        '9,460,730,472,580.801 km',
        '1 ly = 9,460,730,472,580.801 km',
        query='1 light year'
    )


def test_invalidInlineConvert():
    check_inline(
        'Error',
        '@UnitConversionBot',
        description="Sorry, I'm just a stupid bot :-( I don't know what does 'blah' mean. But my master probably does. I'd ask him to teach me.",
        query='10 blah',
    )
