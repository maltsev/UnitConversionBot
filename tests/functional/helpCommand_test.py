# -*- coding: utf-8 -*-
import unittest
from base import FunctionalTestCase, requestTemplate, responseTemplate


class HelpCommandTests(FunctionalTestCase):
    def test_lengthHelp(self):
        self.assertHelp('length', """
- Angstrom `A`
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
- astronomical unit `au`
- light-year `ly`
- parsec `pc`
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
- acre `ac`
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
- Afghan Afghani `afghani`
- Albanian Lek `lek`
- Algerian Dinar DZD
- Angolan Kwanza `kwanza`
- Argentine Peso ARS
- Armenian Dram `dram`
- Aruban Florin `florin`
- Australian Dollar AUD
- Azerbaijani Manat AZN
- Bahamian Dollar BSD
- Bahraini Dinar BHD
- Bangladeshi Taka `taka`
- Barbadian Dollar BBD
- Belarusian Ruble BYR
- Belize Dollar BZD
- Bermudan Dollar BMD
- Bhutanese Ngultrum `ngultrum`
- Bitcoin BTC
- Bolivian Boliviano `boliviano`
- Bosnia-Herzegovina Convertible Mark BAM
- Botswanan Pula `pula`
- Brazilian Real `real`
- British Pound Sterling £
- Brunei Dollar BND
- Bulgarian Lev `lev`
- Burundian Franc BIF
- CFA Franc BCEAO XOF
- CFA Franc BEAC XAF
- CFP Franc XPF
- Cambodian Riel `riel`
- Canadian Dollar C$
- Cape Verdean Escudo `escudo`
- Cayman Islands Dollar KYD
- Chilean Peso CLP
- Chilean Unit of Account (UF) CLF
- Chinese Yuan `yuan`
- Colombian Peso COP
- Comorian Franc KMF
- Congolese Franc CDF
- Costa Rican Colón CRC
- Croatian Kuna `kuna`
- Cuban Convertible Peso CUC
- Cuban Peso CUP
- Czech Republic Koruna `koruna`
- Danish Krone DKK
- Djiboutian Franc DJF
- Dominican Peso DOP
- East Caribbean Dollar XCD
- Egyptian Pound EGP
- Eritrean Nakfa `nakfa`
- Estonian Kroon EEK
- Ethiopian Birr `birr`
- Euro €
- Falkland Islands Pound FKP
- Fijian Dollar FJD
- Gambian Dalasi `dalasi`
- Georgian Lari `lari`
- Ghanaian Cedi `cedi`
- Gibraltar Pound GIP
- Gold (troy ounce) XAU
- Guatemalan Quetzal `quetzal`
- Guernsey Pound GGP
- Guinean Franc GNF
- Guyanaese Dollar GYD
- Haitian Gourde `gourde`
- Honduran Lempira `lempira`
- Hong Kong Dollar HKD
- Hungarian Forint `forint`
- Icelandic Króna ISK
- Indian Rupee `rupee`
- Indonesian Rupiah `rupiah`
- Iranian Rial IRR
- Iraqi Dinar IQD
- Israeli New Sheqel `sheqel`
- Jamaican Dollar JMD
- Japanese Yen ¥
- Jersey Pound JEP
- Jordanian Dinar JOD
- Kazakhstani Tenge `tenge`
- Kenyan Shilling KES
- Kuwaiti Dinar KWD
- Kyrgystani Som KGS
- Laotian Kip `kip`
- Latvian Lats `lats`
- Lebanese Pound LBP
- Lesotho Loti `Loti`
- Liberian Dollar LRD
- Libyan Dinar LYD
- Lithuanian Litas `litas`
- Macanese Pataca `pataca`
- Macedonian Denar `denar`
- Malagasy Ariary `ariary`
- Malawian Kwacha MWK
- Malaysian Ringgit `ringgit`
- Maldivian Rufiyaa `rufiyaa`
- Maltese Lira MTL
- Manx pound IMP
- Mauritanian Ouguiya `ouguiya`
- Mauritian Rupee MUR
- Mexican Peso MXN
- Moldovan Leu MDL
- Mongolian Tugrik `tugrik`
- Moroccan Dirham MAD
- Mozambican Metical `metical`
- Myanma Kyat `kyat`
- Namibian Dollar NAD
- Nepalese Rupee NPR
- Netherlands Antillean Guilder `guilder`
- New Taiwan Dollar TWD
- New Zealand Dollar NZD
- Nicaraguan Córdoba `cordoba`
- Nigerian Naira `naira`
- North Korean Won KPW
- Norwegian Krone NOK
- Omani Rial OMR
- Pakistani Rupee PKR
- Palladium Ounce XPD
- Panamanian Balboa `balboa`
- Papua New Guinean Kina `kina`
- Paraguayan Guarani `guarani`
- Peruvian Nuevo Sol `nuevo sol`
- Philippine Peso PHP
- Platinum Ounce XPT
- Polish Zloty `zloty`
- Qatari Rial QAR
- Romanian Leu RON
- Russian Ruble ₽
- Rwandan Franc RWF
- Saint Helena Pound SHP
- Salvadoran Colón SVC
- Samoan Tala `tala`
- Saudi Riyal `Riyal`
- Serbian Dinar RSD
- Seychellois Rupee SCR
- Sierra Leonean Leone `leone`
- Silver (troy ounce) XAG
- Singapore Dollar SGD
- Solomon Islands Dollar SBD
- Somali Shilling SOS
- South African Rand `rand`
- South Korean Won `won`
- Special Drawing Rights XDR
- Sri Lankan Rupee LKR
- Sudanese Pound SDG
- Surinamese Dollar SRD
- Swazi Lilangeni `lilangeni`
- Swedish Krona SEK
- Swiss Franc Fr
- Syrian Pound SYP
- São Tomé and Príncipe Dobra `dobra`
- Tajikistani Somoni `somoni`
- Tanzanian Shilling TZS
- Thai Baht `Baht`
- Tongan Paʻanga `paanga`
- Trinidad and Tobago Dollar TTD
- Tunisian Dinar TND
- Turkish Lira TRY
- Turkmenistani Manat TMT
- US Dollar $
- Ugandan Shilling UGX
- Ukrainian Hryvnia `hryvnia`
- UAE Dirham AED
- Uruguayan Peso UYU
- Uzbekistan Som UZS
- Vanuatu Vatu `vatu`
- Venezuelan Bolívar Fuerte `bolivar fuerte`
- Vietnamese Dong `dong`
- Yemeni Rial YER
- Zambian Kwacha ZMW
- Zimbabwean Dollar ZWL
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
- foot per hour `ft/h`
- meter per hour `m/h`
- foot per minute `ft/min`
- meter per minute `m/min`
- kilometer per hour `km/h`
- foot per second `ft/s`
- mile per hour `mph`
- knot `kn`
- meter per second `m/s`
- kilometer per minute `km/min`
- mile per minute `mi/min`
- kilometer per second `km/s`
- mile per second `mi/s`
        """)




    def test_timeHelp(self):
        self.assertHelp('time', """
- nanosecond `ns`
- millisecond `ms`
- second `s`
- minute `min`
- hour `h`
- day `d`
- week `wk`
- month `mon`
- year `yr`
        """)




    def test_temperatureHelp(self):
        self.assertHelp('temperature', """
- Celsius `C`
- Fahrenheit `F`
- Kelvin `K`
        """)




    def test_densityHelp(self):
        self.assertHelp('density', """
- gram per cubic meter `g/m3`
- kilogram per cubic meter `kg/m3`
- kilogram per liter `kg/l`
- gram per cubic centimeter `g/cm3`
- gram per milliliter `g/ml`
- tonne per cubic meter `t/m3`
        """)




    def test_informationHelp(self):
        self.assertHelp('information', """
- bit
- kilobit `Kbit`
- megabit `Mbit`
- gigabit `Gbit`
- terabit `Tbit`
- petabit `Pbit`
- exabit `Ebit`
- zettabit `Zbit`
- yottabit `Ybit`

- byte
- kilobyte `KB`
- megabyte `MB`
- gigabyte `GB`
- terabyte `TB`
- petabyte `PB`
- exabyte `EB`
- zettabyte `ZB`
- yottabyte `YB`
        """)




    def test_pressureHelp(self):
        self.assertHelp('pressure', """
- pascal `Pa`
- hectopascal `hPa`
- torr
- kilopascal `kPa`
- pound-force per square inch `psi`
- technical atmosphere `at`
- bar
- standard atmosphere `atm`
- megapascal `MPa`
- kilobar `kbar`
- gigapascal `GPa`
- megabar `Mbar`
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
- length (ft to m)
- area (m² to acre)
- volume (litre to pint)
- currencies ($ to €)
- mass (g to lb)
- speed (km/h to mph)
- time (min to ms)
- temperature (°C to °F)
- density (kg/m³ to g/cm³)
- information (MB to Kbit)
- pressure (atm to Pa)

To get all available units of specific category type "/help #category#" ("/help length", for example).

While asking me a question tet-a-tet you can omit a command. Just type:
- 100 $ to €
- 1 sq foot to m2
- 1 year to hours

While asking me a question in a group please add the command "convert" (if I'm a group member too) or my username "UnitConversionBot":
- /convert 10 yr to mon
- @UnitConversionBot 1 ms to second

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
