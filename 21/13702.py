from typing import *
import sys

input = sys.stdin.readline

def binary_search(pots_max : int) -> int:
    
    left : int = 1
    right : int = pots_max
    result : int = 0

    while left <= right:
        
        mid : int = (left + right) // 2
        ml : int = sum(i // mid for i in pots)
        
        if ml >= K:
            left = mid + 1
            result = mid
        else:
            right = mid - 1

    return result

N , K  = map(int , input().split())
pots = []
for _ in range(N):
    pot : int = int(input())
    pots.append(pot)

print(binary_search(max(pots)))