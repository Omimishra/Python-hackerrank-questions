# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
#You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = list(s)
    result = []

    for i in range(len(s)):
        if i == 0:
            result.append(s[i].upper())
        elif s[i - 1] == ' ':
            result.append(s[i].upper())
        else:
            result.append(s[i])

    result = ''.join(result)
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
