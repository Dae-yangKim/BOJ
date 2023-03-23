from typing import *
from queue import PriorityQueue
import sys

input = sys.stdin.readline

pque = PriorityQueue()

N : int = int(input())
for _ in range(N):
    
    num : int = list(map(int , input().split()))
    
    if num[0] == 0:
        if not pque.empty():
            print(-pque.get())
        else:
            print(-1)
    else:
        for i in num[1:]:
            pque.put(-i)