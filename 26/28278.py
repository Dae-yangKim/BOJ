from typing import *
import sys

input = sys.stdin.readline


class Stack:
    def __init__(self) -> None:
        self.stack = []
    def put(self , X):
        self.stack.append(X)
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    def get(self):
        if self.isEmpty():
            return -1
        else:
            return self.stack.pop(-1)
    def size(self):
        return len(self.stack)
    def boolean(self):
        if self.isEmpty():
            return 1
        else:
            return 0
    def search(self):
        if self.isEmpty():
            return -1
        else:
            return self.stack[-1]
        
stack = Stack()

N : int = int(input())
for _ in range(N):
    
    usr = list(map(int , input().split()))

    if usr[0] == 1:
        stack.put(usr[1])
    elif usr[0] == 2:
        print(stack.get())
    elif usr[0] == 3:
        print(stack.size())
    elif usr[0] == 4:
        print(stack.boolean())
    else:
        print(stack.search())