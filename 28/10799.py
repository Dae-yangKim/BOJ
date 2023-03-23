
from typing import *
import sys

input = sys.stdin.readline

stack = []
usrInput = list(input().rstrip())

count : int = 0

for i in range(len(usrInput)):
    if usrInput[i] == '(':
        stack.append(usrInput[i])
    else:
        if usrInput[i - 1] == '(':
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1
    
print(count)