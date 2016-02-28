from modules.parser import parseRawExpression


class Expression:
    def __init__(self, rawExpressionStr):
        (self.fromUnit, self.toUnit) = parseRawExpression(rawExpressionStr)


    def isValid(self):
        return self.getFromUnit() and self.getToUnit()


    def getFromUnit(self):
        return self.fromUnit


    def getToUnit(self):
        return self.toUnit
