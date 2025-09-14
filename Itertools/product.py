# itertools.product()

# This tool computes the cartesian product of input iterables.
# It is equivalent to nested for-loops.
# For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
# You are given a two lists A and B . Your task is to compute their cartesian product A X B.

# https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
A = list(map(int,input().split())) 
B = list(map(int,input().split())) 
print (*product(A,B))
