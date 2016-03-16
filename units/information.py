# -*- coding: utf-8 -*-

def _getBitNames(prefixSI, prefixIEC):
    prefixFirstLetter = prefixSI[0].upper()

    return [
        prefixFirstLetter + 'bit',
        prefixSI + 'bit', prefixSI + 'bits',
        prefixIEC + 'bit', prefixIEC + 'bits',
        prefixFirstLetter + 'ibit'
    ]


def _getByteNames(prefixSI, prefixIEC):
    prefixFirstLetter = prefixSI[0].upper()

    return [
        prefixFirstLetter + 'B',
        prefixSI + 'byte', prefixSI + 'bytes',
        prefixIEC + 'byte', prefixIEC + 'bytes',
        prefixFirstLetter + 'byte', prefixFirstLetter + 'bytes'
    ]


BIT =      (1,     ['bit', 'bit', 'bits', 'Shannon', 'Shannons'], 'BYTE')
KILOBIT =  (2**10, _getBitNames('kilo', 'kibi'),  'BIT')
MEGABIT =  (2**20, _getBitNames('mega', 'mebi'),  'KILOBIT')
GIGABIT =  (2**30, _getBitNames('giga', 'gibi'),  'MEGABIT')
TERABIT =  (2**40, _getBitNames('tera', 'tebi'),  'GIGABIT')
PETABIT =  (2**50, _getBitNames('peta', 'pebi'),  'GIGABIT')
EXABIT =   (2**60, _getBitNames('exa', 'exbi'),   'GIGABIT')
ZETTABIT = (2**70, _getBitNames('zetta', 'zebi'), 'GIGABIT')
YOTTABIT = (2**80, _getBitNames('yotta', 'yobi'), 'GIGABIT')

BYTE =      (BIT[0] * 8, ['byte', 'byte', 'bytes'], 'BIT')
KILOBYTE =  (KILOBIT[0] * 8,  _getByteNames('kilo', 'kibi'),  'BYTE')
MEGABYTE =  (MEGABIT[0] * 8,  _getByteNames('mega', 'mebi'),  'KILOBYTE')
GIGABYTE =  (GIGABIT[0] * 8,  _getByteNames('giga', 'gibi'),  'MEGABYTE')
TERABYTE =  (TERABIT[0] * 8,  _getByteNames('tera', 'tebi'),  'GIGABYTE')
PETABYTE =  (PETABIT[0] * 8,  _getByteNames('peta', 'pebi'),  'GIGABYTE')
EXABYTE =   (EXABIT[0] * 8,   _getByteNames('exa', 'exbi'),   'GIGABYTE')
ZETTABYTE = (ZETTABIT[0] * 8, _getByteNames('zetta', 'zebi'), 'GIGABYTE')
YOTTABYTE = (YOTTABIT[0] * 8, _getByteNames('yotta', 'yobi'), 'GIGABYTE')


_BASE = 'BIT'
