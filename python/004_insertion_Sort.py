#!/bin/python
#coding=utf-8
import math
import os
import random
import re
import sys



# Complete the findNumber function below.
def InsertionSort(arr):
    for i in range(0,len(arr)-1):
        curNum, preIndex = arr[i+1], i  # curNum 保存当前待插入的数
        while preIndex >= 0 and curNum < arr[preIndex]: # 将比 curNum 大的元素向后移动
            arr[preIndex + 1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex + 1] = curNum  # 待插入的数的正确位置   
    return arr
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input().strip())

    arr = []

    for _ in xrange(arr_count):
        arr_item = int(raw_input().strip())
        arr.append(arr_item)

    res = InsertionSort(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
