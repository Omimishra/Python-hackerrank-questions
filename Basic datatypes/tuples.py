# Given an integer,n , and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t) .
# https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split()) #input() returns a string, map converts it to an iterable of integers
    print(hash(tuple(integer_list)))
