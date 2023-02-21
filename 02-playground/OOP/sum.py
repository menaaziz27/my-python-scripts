#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    #
    return sum(ar)

if __name__ == '__main__':

	length = int(input())
	lis =[int(input()) for i in range(length)]

	print(simpleArraySum(lis))
