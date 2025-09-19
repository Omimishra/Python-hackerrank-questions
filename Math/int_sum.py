# Read four numbers,a ,b ,c , and d, and print the result of a^b+c^d.
# https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = int(input())
c = int(input())
d = int(input())

Sum = (pow(a,b) + pow(c,d))
print(Sum)
