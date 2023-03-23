from typing import *
import sys

input = sys.stdin.readline

def solution(arr) -> int:
    global J
    count : int = 0
    for num in arr:
        J -= num
        count += 1
        
        if J <= 0:
            return count

T : int = int(input())

for _ in range(T):
    arr = []
    J , N = map(int , input().split())
    for _ in range(N):
        R , C = map(int , input().split())
        arr.append(R * C)
    
    print(solution(sorted(arr , reverse = True)))