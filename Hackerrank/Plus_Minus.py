#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    count = len(arr)
    pos =0
    neg = 0
    zero =0
    for i in arr:
        #print(i)
        #count+=1
        if i==0:
            zero+=1
        elif i>0:
            pos+=1
        else:
            neg+=1
    print("{:.6f}".format(pos/count) )
    print("{:.6f}".format(neg/count) )
    print("{:.6f}".format(zero/count) )
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)