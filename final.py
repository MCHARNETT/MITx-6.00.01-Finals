# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 14:43:00 2017

@author: harne
"""

import sys

def getRecord(s):
    # Complete this function
    low = min(s[0:2])
    high = max(s[0:2])
    
    low_count = 0
    high_count = 0
    
    for item in s:
        if item>high:
            high = item
            high_count += 1
        elif item<low:
            low = item
            low_count += 1
    return high_count, low_count

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
