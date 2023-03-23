from typing import *
import sys

input = sys.stdin.readline

stack = []
bracket = input().rstrip()

for brac in bracket:
    stack.append(brac)
    length = len(stack)
    
    if length > 1 and stack[length - 1] == ')' and stack[length - 2] == '(':
        stack.pop()
        stack.pop()
    
print(len(stack))