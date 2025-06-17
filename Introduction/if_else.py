#https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n%2!=0: #If  is odd, print Weird
    print("Weird")
elif ((n%2==0) and 2 <= n <= 5): #If  is even and in the inclusive range of 2 to 5, print Not Weird
    print("Not Weird")
elif ((n%2==0) and 6<=n<=20): #If  is even and in the inclusive range of 6 to 20, print Weird
    print("Weird")
elif ((n%2==0) and n>20):#If  is even and greater than 20, print Not Weird
    print("Not Weird")
else:
    print("Weird")
