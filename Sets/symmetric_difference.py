# Given 2 sets of integers,M  and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

# https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
a=set(map(int,input().split()))
n=int(input())
b=set(map(int,input().split()))
a_b=sorted(a.symmetric_difference(b))
for num in a_b:
    print(num)
