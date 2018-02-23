#!/usr/bin/env python

from __future__ import print_function
import sys, os
import requests
import config

## =============================================================================

class AuthenticationError(Exception):
    pass

def authenticate():
    try:
        headers = {'Content-Type' : 'application/json'
                  ,'Accept' : 'application/json'
                  ,'User-Agent' : config.userAgent
                  }
        data = {'accountName' : os.environ['USER']
               ,'password': os.environ['PASS']
               ,'applicationId' : config.applicationID
               }

        resp = requests.post(config.authenticateURL, headers=headers, json=data)
        if resp.status_code != requests.codes.ok:
            raise AuthenticationError('error getting authentication key')

        return resp.json()
    except NameError:
        raise EnvironmentError('credentials not set up')

def test(event, context):
    auth = authenticate()
    print("auth key: ", auth)
    return auth

if __name__ == '__main__':
    sys.exit(test(None, None))

