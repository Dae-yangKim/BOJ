from typing import *
import sys

input = sys.stdin.readline

def solution(arr : List[int]) -> int:
    arr = sorted(arr , reverse = True)

    count : int = 0
    value : int = 0

    for i in range(len(arr)):
        count += (arr[i] + N >= value)
        value = max(value , arr[i] + i + 1)
    
    return count
N : int = int(input())
arr : List[int] = []
for i in range(N):
    n : int = int(input())
    arr.append(n)
result : int = solution(arr) ; print(result)