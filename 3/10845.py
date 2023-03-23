import sys
from collections import deque as dq

input = sys.stdin.readline

deq = dq()

num = int(input())

for i in range(num):
    usr_input = input().split()

    if usr_input[0] == "push":
        deq.append(usr_input[1])
    elif usr_input[0] == "pop":
        if len(deq) == 0:
            print(-1)
            continue
    
        value = deq.popleft()
        print(value)
    elif usr_input[0] == "size":
        print(len(deq))
    elif usr_input[0] == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif usr_input[0] == "front":
        if len(deq) == 0:
            print(-1) ; continue
        
        print(deq[0])
    else:
        if len(deq) == 0:
            print(-1) ; continue
        
        print(deq[-1])