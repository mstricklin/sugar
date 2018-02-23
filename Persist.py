#!/usr/bin/env python
# CLASSIFICATION NOTICE: This file is UNCLASSIFIED

from __future__ import print_function
import sys
import boto3

import config

## =============================================================================
res = boto3.resource('dynamodb', region_name=config.awsRegion)

table = res.Table(config.tableName)

# value needs to be a dict, including keys that match the HASH and RANGE keys,
# which are "day" and "system time"
def persist(value):
    response = table.put_item(Item=value.dict())

def test():
    pass

if __name__ == '__main__':
    sys.exit(test())

