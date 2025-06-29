import sys

sys.path.append(".")
from chalicelib.modules.parser import parseExpression, parseMessageText  # noqa: E402
from chalicelib.modules.converter import convertUnit  # noqa: E402
from chalicelib.modules.formatter import formatValueUnit  # noqa: E402
from chalicelib import units  # noqa: E402

if len(sys.argv) < 2:
    expressions = [line.strip() for line in sys.stdin]
else:
    expressions = [" ".join(sys.argv[1:]).strip()]

unitsIndex = units.getIndex()
for expression in expressions:
    try:
        units = parseExpression(parseMessageText(expression)["expression"], unitsIndex)
        toValueUnit = convertUnit(units["fromValueUnit"], units["toUnit"])
        print(f"{expression}: {formatValueUnit(toValueUnit)}")
    except Exception as error:
        print("{:32s} {}".format(error.__class__.__name__, expression))
