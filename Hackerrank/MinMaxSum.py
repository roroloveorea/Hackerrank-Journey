#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    max=0
    min=10000000000000000000000000000000000
    for i in arr:
        
        if i < min:
            min=i
        if i > max:
            max =i
        
            
    maxsum =0
    minsum=0
    for i in arr:
        if i != min:
            maxsum+=i
        if i != max:
            minsum+=i
        if max == min:
            minsum = maxsum = 4*max
    print(minsum , maxsum)
    #print(min)
    #print(max)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
