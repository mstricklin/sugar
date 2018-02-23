#!/usr/bin/env python

from __future__ import print_function
import sys, os
import requests
import config

## =============================================================================

def getValues():
    try:
        headers = {'Content-Type' : 'application/json'
                  ,'Accept' : 'application/json'
                  ,'User-Agent' : config.userAgent
                  }
        params = {'minutes': config.minutes
                 ,'maxCount': config.maxCount
                 ,'sessionId': config.AUTH_TOKEN
                 }

        resp = requests.post(config.getDataURL, headers=headers, params=params)

        return resp.json()
    except NameError:
        raise EnvironmentError('credentials not set up')

def test(event, context):
    auth = authenticate()
    print("auth key: ", auth)
    return auth

if __name__ == '__main__':
    sys.exit(test(None, None))

