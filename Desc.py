#!/usr/bin/env python

from __future__ import print_function
import sys

import boto3

## =============================================================================
def desc(event, context):
    dynamoClient = boto3.client('dynamodb', region_name='us-east-2')

    print( dynamoClient.describe_table(TableName='sugar') )


def main(argv=None):
    if argv is None:
        argv = sys.argv
    print("Hello, world")

if __name__ == '__main__':
    sys.exit(main())

