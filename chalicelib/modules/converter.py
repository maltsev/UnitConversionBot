def convertUnit(fromValueUnit, toUnit):
    fromUnit = fromValueUnit["unit"]

    if fromUnit["category"] != toUnit["category"]:
        errorMessage = f"Sorry, I can't convert {fromUnit['baseName']} to {toUnit['baseName']} (at least in this universe)."
        raise IncompatibleCategoriesException(errorMessage)

    if fromUnit["category"] == "temperature":
        baseUnitToValue = fromUnit["convertToBase"](fromValueUnit["value"])
        toValue = toUnit["convertFromBase"](baseUnitToValue)
    else:
        toValue = (fromValueUnit["value"] * fromUnit["value"]) / toUnit["value"]

    toValueUnit = {"value": toValue, "unit": toUnit}

    return toValueUnit


class IncompatibleCategoriesException(Exception):
    pass
