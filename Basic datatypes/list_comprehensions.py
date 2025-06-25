# You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n. 
# https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    res = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range (z+1):
                if(i+j+k!=n):
                    res.append([i,j,k])
    print (res)
                
