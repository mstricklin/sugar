#!/usr/bin/env python

from __future__ import print_function
import sys
from time import time

values = dict()


## =============================================================================
class Rule(object):
    def __init__(self, name):
        self.name = name
        self.rules = []
        self.actions = []
    def check(self, test):
        self.rules.append(test)
        return self
    def action(self, action):
        self.actions.append(action)
        return self
    def test(self, data):
        if all(r.test(data) for r in self.rules):
            [a.action(data) for a in self.actions]
## =============================================================================
def lastDatapoint(data):
    return sorted(data)[-1]
## =============================================================================

# True if last data point is within 'window' seconds
class RecentData(object):
    def __init__(self, window):
        self.window = window
    def test(self, data):
        try:
            last = lastDatapoint(data)
            now = int(time())
            if (last.timestamp()+self.window >= now):
                return True
        except IndexError:
            pass
        return False

# true if last datapoint is between low and high
class Range(object):
    def __init__(self, low, high):
        self.low = low
        self.high = high
    def test(self, data):
        try:
            last = lastDatapoint(data)
            return self.low <= last.value() <= self.high
        except IndexError:
            pass
        return False

# returns True every 'window' seconds
class Dampen(object):
    def __init__(self, window):
        self.window = window
        self.last_alert = 0
    def test(self, data):
        now = int(time())
        if (self.last_alert + window <= now):
            self.last_alert = now
            return True
        return False

# returns True every 'window' seconds
class Trend(object):
    def __init__(self, trend_value):
        self.trend_value = trend_value
    def test(self, data):
        try:
            last = lastDatapoint(data)
            return self.trend_value == last.trend()
        except IndexError:
            pass
        return False



## =============================================================================
# have within window (RecentData)
# value between hi & low (InRange)
# trend is xxx (Trend)
# not triggered in past xxx (Dampen)
# then alert (Alert)


def main(argv=None):
    import json
    from Data import cleanRepr
    import sample_data

    r = Rule('sam').check(RecentData(450)).check(Range(100, 300)).check(Trend('2 down'))
    values = set()
    data = json.loads(sample_data.jsonStr)
    values.update(cleanRepr(data))
    print(values)
    for d in values:
        print(d)
    r.test(values)


if __name__ == '__main__':
    sys.exit(main())

