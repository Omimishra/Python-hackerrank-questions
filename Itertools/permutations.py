# You are given a string S.
# Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

# https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s,k=input().split()
for i in permutations(sorted(s),int(k)):
    print(''.join(i))
