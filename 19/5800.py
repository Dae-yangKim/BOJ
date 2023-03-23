from typing import *
import sys

input = sys.stdin.readline

def solution(arr : List[int]):
    
    top : int = max(arr)
    low : int = min(arr)
    
    arr = sorted(arr , reverse=True)
    
    gap : int = 0
    for idx in range(len(arr) - 1):
        
        num = arr[idx] - arr[idx + 1]

        if num > gap:
            gap = num
    
    return (top , low , gap)

N : int = int(input())

for i in range(N):
    arr : List[int] = list(map(int , input().split()))
    top , low , gap = solution(arr[1 :])

    print(f"Class {i + 1}")
    print(f"Max {top}, Min {low}, Largest gap {gap}")