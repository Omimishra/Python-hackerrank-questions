# You are given an integer, N. Your task is to print an alphabet rangoli of size N.
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true
import math


def get_char_seq(j, n):
    str1 = ''
    for i in range(1, j + 1):
        str1 += chr(97 + n - i)
    str1 = '-'.join(str1)
    return str1

def get_string(i,size,columns):
        str1 = get_char_seq(i, size)
        str2 = str1[:-2]
        str2 = ''.join(reversed(str2))
        left_dash = ((math.floor(columns / 2) + 1) - len(str1)) * '-'
        right_dash = ((math.floor(columns / 2) - 1) - len(str2)) * '-'
        full_string=left_dash + str1 + '-' + str2 + right_dash
        return full_string
        
def print_rangoli(size):
    # your code goes here
    columns = 4 * size - 3
    if size==1:
        print('a')
    else:
      for i in range(1, size + 1):
        full_string=get_string(i,size,columns)
        print(full_string)
      for i in range(size - 1, 0, -1):
        full_string=get_string(i,size,columns)
        print(full_string)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)