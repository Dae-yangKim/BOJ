from typing import *
import sys

input = sys.stdin.readline

def solution(N : int) -> int:
    line : int = N + 1
    point : int = 0
    plus : int = 0

    for i in range(1 , N + 1):
        point += plus        
        
        if i % 3 == 0:
            continue
        else:
            plus += 1

    return line + point

N : int = int(input())
print(solution(N))