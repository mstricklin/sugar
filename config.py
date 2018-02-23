#!/usr/bin/env python

from collections import defaultdict

## =============================================================================

AUTH_TOKEN = None
awsRegion='us-east-2'
tableName='sugar'
timezone = 'America/Chicago'

authenticateURL = 'https://share1.dexcom.com/ShareWebServices/Services/General/LoginPublisherAccountByName'
userAgent = 'Dexcom Share/3.0.2.11 CFNetwork/711.2.23 Darwin/14.0.0'
applicationID = 'd8665ade-9673-4e27-9ff6-92db4ce13d13'

getDataURL = 'https://share1.dexcom.com/ShareWebServices/Services/Publisher/ReadPublisherLatestGlucoseValues'
minutes=1440 # 24 hours
maxCount=144 # 12 hours at every 5 minutes

trend_text=defaultdict(lambda: '<missing>',
                      {0: '',
                       1: '2 up',
                       2: 'up',
                       3: 'angle up',
                       4: 'flat',
                       5: 'angle down',
                       6: 'down',
                       7: '2 down',
                       8: 'no trend',
                       9: 'unavailable'})

