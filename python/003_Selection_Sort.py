#!/bin/python

import math
import os
import random
import re
import sys



# Complete the findNumber function below.
def BubbleSort(arr, k):
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                temp = arr [i]
                arr[i] = arr[j]
                arr[j] = temp

        
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input().strip())

    arr = []

    for _ in xrange(arr_count):
        arr_item = int(raw_input().strip())
        arr.append(arr_item)

    k = int(raw_input().strip())

    res = BubbleSort(arr, k)

    fptr.write(str(res) + '\n')

    fptr.close()
