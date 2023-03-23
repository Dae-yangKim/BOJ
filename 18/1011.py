from typing import *
import sys

input = sys.stdin.readline

def solution(x : int , y : int) -> int:
    
    distance : int = y - x
    num : int = 0

    while True:
        
        if distance <= num * (num + 1):
            break
        
        num += 1
    
    if distance <= num**2:
        return (num * 2 - 1)
    else:
        return (num * 2)
    
N : int = int(input())
for _ in range(N):
    
    x , y = map(int , input().split())
    print(solution(x , y))