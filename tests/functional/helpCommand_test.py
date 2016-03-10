# -*- coding: utf-8 -*-
import os
import unittest
from base import FunctionalTestCase, requestTemplate, responseTemplate


class HelpCommandTests(FunctionalTestCase):
    def test_lengthHelp(self):
        self.assertHelp('length', """
- nanometer `nm`
- micrometer `um`
- millimeter `mm`
- centimeter `cm`
- inch `in`
- decimeter `dm`
- foot `ft`
- yard `yd`
- meter `m`
- hectometer `hm`
- kilometer `km`
- mile `mi`
- nautical mile `nmi`
        """)




    def test_areaHelp(self):
        self.assertHelp('area', """
- square nanometer `nm2`
- square millimeter `mm2`
- square centimeter `cm2`
- square inch `in2`
- square decimeter `dm2`
- square foot `ft2`
- square yard `yd2`
- square meter `m2`
- hectare `ha`
- square kilometer `km2`
- square mile `mi2`
        """)




    def test_volumeHelp(self):
        self.assertHelp('volume', """
- cubic nanometer `nm3`
- cubic millimeter `mm3`
- cubic centimeter `cm3`
- milliliter `ml`
- cubic inch `in3`
- imperial fluid ounce `fl.oz`
- imperial pint `pt`
- cubic decimeter `dm3`
- liter `l`
- imperial quart `qt`
- imperial gallon `gal`
- cubic foot `ft3`
- cubic yard `yd3`
- cubic meter `m3`
- cubic kilometer `km3`
- cubic mile `mi3`
        """)




    def test_currenciesHelp(self):
        self.assertHelp('currencies', u"""
- Canadian dollar `C$`
- Russian ruble `₽`
- Swiss franc `Fr`
- US dollar `$`
- euro `€`
- pound sterling `£`
- yen `¥`
- yuan `yuan`
        """)




    def test_massHelp(self):
        self.assertHelp('mass', """
- nanogram `ng`
- microgram `ug`
- milligram `mg`
- gram `g`
- ounce `oz`
- pound `lb`
- kilogram `kg`
- tonne `t`
        """)




    def test_speedHelp(self):
        self.assertHelp('speed', """
- kilometer per hour `km/h`
- foot per second `ft/s`
- mile per hour `mph`
- knot `kn`
- meter per second `m/s`
        """)




    def test_timeHelp(self):
        self.assertHelp('time', """
- millisecond `ms`
- second `s`
- minute `min`
- hour `h`
- day `d`
- week `wk`
- month `mon`
- year `yr`
        """)




    def test_defaultHelp(self):
        requestJson = requestTemplate({
            'text': '/help',
            'chat': {
                'id': 8654
            }
        })

        expectedResponseJson = responseTemplate({
            'chat_id': 8654,
            'parse_mode': 'Markdown',
            'text': u"""
The bot supports following unit categories:
- length
- area
- volume
- currencies
- mass
- speed
- time

To get all available units of specific category type "/help #category#" ("/help length", for example).

While asking me a question tet-a-tet you can omit a command. Just type:
- 100 $ to €
- 1 sq foot to m2
- 1 year to hours

While asking me a question in a group please add the command "convert" (if I'm a group member too) or my username "UserConversionBot":
- /convert 10 yr to mon
- @UserConversionBot 1 ms to second

You can also ask me without adding me to the chat. Just type '@UnitConversionBot 100 ft to m' when you need my help.

You can use both short (`m2`) and full unit names (square meter).


If you have an issue or just want to say thanks, feel free to contact my master @kirillmaltsev
Thank you for chatting with me :-)
            """.strip()
        })

        self.assertRequest(requestJson, expectedResponseJson)




    def assertHelp(self, unitsCategory, expectedUnits):
        requestJson = requestTemplate({
            'text': '/help ' + unitsCategory,
            'chat': {
                'id': 8654
            }
        })

        expectedText = u'*The full list of {} units:*\n'.format(unitsCategory)
        expectedText += expectedUnits.strip()

        expectedResponseJson = responseTemplate({
            'chat_id': 8654,
            'parse_mode': 'Markdown',
            'text': expectedText
        })

        self.assertRequest(requestJson, expectedResponseJson)
