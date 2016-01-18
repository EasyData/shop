#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# merge two json files
#

import json
import sys

def load(path):
    d = {}
    with open(path) as f:
        for line in f:
            obj = json.loads(line)
            d[obj['id']] = obj
    return d

def merge(left, right):
    for k1, v1 in left.iteritems():
        if k1 in right:
            v2 = right[k1]
            yield {
                'id': k1,
                v1['lang']: v1,
                v2['lang']: v2,
            }

if __name__ == '__main__':
    for i in merge(load(sys.argv[1]), load(sys.argv[2])):
        print(json.dumps(i))

