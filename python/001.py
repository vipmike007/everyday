#!/bin/python

import math
import os
import random
import re
import sys



# Complete the findNumber function below.
def findNumber(arr, k):
    res = 'NO'
    for i in arr:
        if i == k:
            res = 'YES'

        
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input().strip())

    arr = []

    for _ in xrange(arr_count):
        arr_item = int(raw_input().strip())
        arr.append(arr_item)

    k = int(raw_input().strip())

    res = findNumber(arr, k)

    fptr.write(res + '\n')

    fptr.close()
