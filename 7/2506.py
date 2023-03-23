from typing import *
import sys

input = sys.stdin.readline

def solution(arr : List[int]) -> List[int]:
    scores : List[int] = []
    count : int = 0

    for i in arr:
        if i == 1:
            count += 1
            scores.append(count)
        else:
            count = 0

    return scores

N : int = int(input())
arr : List[int] = list(map(int , input().split()))
scores : List[int] = solution(arr)
print(sum(scores))