# -*- coding: utf-8 -*-
import os
import unittest
from base import FunctionalTestCase, requestTemplate, responseTemplate

helpMessage = u"""
*Full list of available units:*
*Area*
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

*Volume*
- cubic nanometer `nm3`
- cubic millimeter `mm3`
- cubic centimeter `cm3`
- milliliter `ml`
- cubic inch `in3`
- imperial fluid ounce `fl.oz`
- imperial pint `pt`
- liter `l`
- cubic decimeter `dm3`
- imperial quart `qt`
- imperial gallon `gal`
- cubic foot `ft3`
- cubic yard `yd3`
- cubic meter `m3`
- cubic kilometer `km3`
- cubic mile `mi3`

*Currency*
- Canadian dollar `C$`
- Russian ruble `₽`
- Swiss franc `Fr`
- US dollar `$`
- euro `€`
- pound sterling `£`
- yen `¥`
- yuan `yuan`

*Length*
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

*Mass*
- nanogram `ug`
- milligram `mg`
- gram `g`
- ounce `oz`
- pound `lb`
- kilogram `kg`
- tonne `t`

*Time*
- millisecond `ms`
- second `s`
- minute `min`
- hour `h`
- day `d`
- week `wk`
- month `mon`
- year `yr`

*Speed*
- kilometer per hour `km/h`
- foot per second `ft/s`
- mile per hour `mph`
- knot `kn`
- meter per second `m/s`


While asking me a question tet-a-tet you can omit a command. Just type:
- 100 $ to €
- 1 sq foot to m2
- 1 year to hours

While asking me a question in a group please add the command "convert" (if I'm a group member too) or my username "UserConversionBot":
- /convert 10 yr to mon
- @UserConversionBot 1 ms to second

You can use both short (`m2`) and full unit names (square meter).


If you have an issue or just want to say thanks, feel free to contact my master @kirillmaltsev
Thank you for chatting with me :-)""".strip()


class HelpCommandTests(FunctionalTestCase):
    def test_help(self):
        requestJson = requestTemplate({
            'text': '/help help',
            'chat': {
                'id': 8654
            }
        })

        expectedResponseJson = responseTemplate({
            'chat_id': 8654,
            'parse_mode': 'Markdown',
            'text': helpMessage
        })

        if os.environ['RUN_ON_INSTANCE']:
            responseData = self.makeRequest(requestJson)
            self.assertEqual(responseData['response'].status_code, 200)
            self.assertEqual(responseData['contentType'], 'application/json')
            self.assertTrue('You can use both short ' in responseData['json']['text'])
            self.skipTest('Some unicode issue')
        else:
            self.assertRequest(requestJson, expectedResponseJson)
