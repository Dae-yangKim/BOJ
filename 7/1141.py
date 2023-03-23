from typing import *
import sys

input = sys.stdin.readline

def solution(arr : List[int]) -> int:
    arr = list(set(arr))
    count : int = 0
    for i in range(len(arr)):
        sentence : str = arr[i] ; length_sentence : int = len(sentence)
        for idx in range(len(arr)):
            if sentence == arr[idx]: continue
            if sentence == arr[idx][:length_sentence]:
                count += 1 ; break
    return len(arr) - count
    
N : int = int(input())
arr : List[str] = []
for i in range(N):
    sentence : str = input().strip(); arr.append(sentence)
result : int = solution(arr)
print(result)