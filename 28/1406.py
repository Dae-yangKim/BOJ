from typing import *
import sys

input = sys.stdin.readline

s_1 = list(input().rstrip())
s_2 = []

N : int = int(input())
for _ in range(N):

    usrInput = list(input().rstrip().split())
    
    if usrInput[0] == 'L':
        if s_1:
            s_2.append(s_1.pop())
    elif usrInput[0] == 'D':
        if s_2:
            s_1.append(s_2.pop())
    elif usrInput[0] == 'B':
        if s_1:
            s_1.pop()
    else:
        s_1.append(usrInput[1])

s_1.extend(reversed(s_2))
print("".join(s_1))