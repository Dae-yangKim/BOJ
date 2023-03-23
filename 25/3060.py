from typing import *
import sys

input = sys.stdin.readline

T : int = int(input())
for _ in range(T):
    N : int = int(input())
    arr = sum(list(map(int , input().split())))
    day = 1
    
    while N >= arr:
        day += 1
        arr *= 4
    
    print(day)