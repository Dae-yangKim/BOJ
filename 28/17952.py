
from typing import *
import sys

input = sys.stdin.readline

stack = []
point : int = 0

N : int = int(input())
for _ in range(N):
    usrInput = list(map(int , input().split()))

    if usrInput[0] == 1:
        stack.append((usrInput[1] , usrInput[2]))
    
    if stack:
        s , t = stack.pop()
        t -= 1
        if t == 0:
            point += s
        else:
            stack.append((s , t))

print(point)