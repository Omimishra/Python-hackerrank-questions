# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.
# https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
import math
N , M = map(int, input().split())
# M = 3*N  #because it will be done implicitly by hackerank, no need to ovrwrite

ro = math.floor(N/2)
for i in range(0 ,ro):
    print(('.|.'*(i*2+1)).center(M,'-'))
    
print('WELCOME'.center(M,'-'))

for i in range(ro-1,-1,-1):
    print(('.|.'*(i*2+1)).center(M,'-'))
