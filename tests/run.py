# -*- coding: utf-8 -*-
import sys
import os
import platform
sys.path.append('.')

if 'GAE_BASE_PATH' in os.environ:
    GAE_BASE_PATH = os.environ['GAE_BASE_PATH']
elif platform.system() == 'Darwin':
    GAE_BASE_PATH = '/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine'
else:
    print 'Set GAE_BASE_PATH'
    sys.exit(1)

sys.path.append(GAE_BASE_PATH + '/lib/webapp2-2.3')
sys.path.append(GAE_BASE_PATH)

RUN_ON_INSTANCE = '--instance' in sys.argv
os.environ['RUN_ON_INSTANCE'] = '1' if RUN_ON_INSTANCE else ''
os.environ['DEBUG'] = '1'

import unittest
import unit
import functional
import units

units.getIndex(True, stubExchangeRate=True)

alltests = unittest.TestSuite()
if not RUN_ON_INSTANCE:
    alltests.addTests(unit.tests)

alltests.addTests(functional.tests)

if __name__ == '__main__':
    result = unittest.TextTestRunner().run(alltests)
    if not result.wasSuccessful():
        sys.exit(1)
