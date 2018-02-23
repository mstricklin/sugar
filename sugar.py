#!/usr/bin/env python
# CLASSIFICATION NOTICE: This file is UNCLASSIFIED

from __future__ import print_function
import sys
import config

from Authorize import authenticate
from Get import getValues
from Data import cleanRepr
from Persist import persist

## =============================================================================

Values = set()


def handler(event, context):
    for retry in (1,2,3):
        try:
            if config.AUTH_TOKEN is None:
                config.AUTH_TOKEN = authenticate()
            for value in cleanRepr(getValues()):
                if value not in Values:
                    persist(value)
                    Values.add(value)
            return True
        except EnvironmentError as e:
            config.AUTH_TOKEN = None
            print('failure', e)
    print('retry failure', e)
    return False

def test(event, context):
    handler(event, context)
    return None


if __name__ == '__main__':
    sys.exit(test(None, None))

