from math import pi as _PI

ANGSTROM = (
    1e-10,
    ["A", "Angstrom", "Angstroms", "ångström", "Ångström", "Å"],
    "NANOMETER",
)
NANOMETER = (
    1e-9,
    ["nm", "nanometer", "nanometers", "nanometre", "nanometres"],
    "MICROMETER",
)
# Main symbol — µ (U+00B5), second — μ (U+03BC)
MICROMETER = (
    1e-6,
    ["µm", "micrometer", "micrometers", "micrometre", "micrometres", "μm", "um"],
    "MILLIMETER",
)
MILLIMETER = (
    0.001,
    ["mm", "millimeter", "millimeters", "millimetre", "millimetres"],
    "CENTIMETER",
)
CENTIMETER = (
    0.01,
    ["cm", "centimeter", "centimeters", "centimetre", "centimetres"],
    "METER",
)
DECIMETER = (0.1, ["dm", "decimeter", "decimeters", "decimetre", "decimetres"], "METER")
METER = (1, ["m", "meter", "meters", "metre", "metres"], "FOOT")
HECTOMETER = (
    100,
    ["hm", "hectometer", "hectometers", "hectometre", "hectometres"],
    "METER",
)
KILOMETER = (1000, ["km", "kilometer", "kilometers", "kilometre", "kilometres"], "MILE")

INCH = (0.0254, ["in", "inch", "inches"], "CENTIMETER")
FOOT = (INCH[0] * 12, ["ft", "foot", "feet"], "METER")
YARD = (INCH[0] * 36, ["yd", "yard", "yards"], "METER")
MILE = (FOOT[0] * 5280, ["mi", "mile", "miles"], "KILOMETER")

NAUTICAL_MILE = (1852, ["nmi", "nautical mile", "nautical miles"], "KILOMETER")

ASTRONOMICAL_UNIT = (
    149597870700,
    ["au", "astronomical unit", "astronimical units", "ua"],
    "KILOMETER",
)
RACK_UNIT = (0.04445, ["U", "rack unit", "rack units", "unit", "units"], "CENTIMETER")
PARSEC = (
    (648000 * ASTRONOMICAL_UNIT[0]) / _PI,
    ["pc", "parsec", "parsecs"],
    "KILOMETER",
)
LIGHT_YEAR = (
    9460730472580800,
    [
        "ly",
        "light-year",
        "light-years",
        "light year",
        "light years",
        "lightyear",
        "lightyears",
    ],
    "KILOMETER",
)

_BASE = "METER"
