# -*- coding: utf-8 -*-
from __future__ import division as _
import area as _a

PASCAL =      (1, ['Pa', 'pascal', 'pascals'], 'HECTOPASCAL')
HECTOPASCAL = (100, ['hPa', 'hectopascal', 'hectopascals'], 'PASCAL')
KILOPASCAL =  (1000, ['kPa', 'kilopascal', 'kilopascals'], 'PASCAL')
MEGAPASCAL =  (1e6, ['MPa', 'megapascal', 'megapascals'], 'PASCAL')
GIGAPASCAL =  (1e9, ['GPa', 'gigapascal', 'gigapascals'], 'PASCAL')

BAR =                   (1e5, ['bar', 'bar', 'bars'], 'STANDARD_ATMOSPHERE')
KILOBAR =               (BAR[0]*1e3, ['kbar', 'kilobar', 'kilobars'], 'POUND_PER_SQUARE_INCH')
MEGABAR =               (BAR[0]*1e6, ['Mbar', 'megabar', 'megabars'], 'POUND_PER_SQUARE_INCH')

TECHNICAL_ATMOSPHERE =  (98066.5, ['at', 'technical atmosphere', 'technical atmospheres'], 'BAR')
STANDARD_ATMOSPHERE =   (101325, ['atm', 'standard atmosphere', 'standard atmospheres'], 'BAR')
TORR =                  (STANDARD_ATMOSPHERE[0] / 760, ['Torr', 'torr', 'torrs'], 'BAR')
POUND_PER_SQUARE_INCH = (4.4482 / _a.INCH_SQUARE[0], ['psi', 'pound-force per square inch', 'pound-forces per square inch', 'pound per square inch', 'pounds per square inch', 'lbf/in2', 'lnf/sq in'], 'BAR')
