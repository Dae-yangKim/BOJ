from typing import *
from collections import deque
import sys

input = sys.stdin.readline

deque = Deque()

N : int = int(input())
for _ in range(N):
    
    usrInput = list(map(int , input().split()))

    if usrInput[0] == 1:
        deque.appendleft(usrInput[1])
    elif usrInput[0] == 2:
        deque.append(usrInput[1])
    elif usrInput[0] == 3:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft())
    elif usrInput[0] == 4:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    elif usrInput[0] == 5:
        print(len(deque))
    elif usrInput[0] == 6:
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif usrInput[0] == 7:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    else:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])