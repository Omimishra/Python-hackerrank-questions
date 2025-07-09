# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.
# https://www.hackerrank.com/challenges/python-lists/copy-from/436204733
if __name__ == '__main__':
    n = int(input())
    nums=[]
    for i in range(n):
        cmd=input().split()
        if(cmd[0]=='insert'):
            nums.insert(int(cmd[1]),int(cmd[2]))
        if(cmd[0]=='print'):
            print(nums)
        if(cmd[0]=='remove'):
            nums.remove(cmd[1])
        if(cmd[0]=='append'):
            nums.append(int(cmd[1]))
        if(cmd[0]=='sort'):
            nums.sort()
        if(cmd[0]=='pop'):
            nums.pop()
        if(cmd[0]=='reverse'):
            nums.reverse()
