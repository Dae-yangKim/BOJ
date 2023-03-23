from typing import *
import sys

input = sys.stdin.readline

def solution(N : int , K : int) -> int:
    arr : List[int] = [0]

    for i in range(1 , N + 1):
        if N % i == 0:
            arr.append(i)
        else : continue

    if len(arr[1 : ]) < K:
        return 0
    else:
        return arr[K]

N , K = map(int , input().split())
print(solution(N , K))