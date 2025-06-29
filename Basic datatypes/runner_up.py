# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # for storing the unique values
    set_arr=set(arr) 
    # sorting the unique values
    sorted_arr=sorted(set_arr) 
    # and printing the second last element
    print(sorted_arr[len(sorted_arr)- 2])
