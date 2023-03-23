from typing import *
import sys

input = sys.stdin.readline

def binary_search(N : int) -> int:
    
    left : int = 1
    right : int = N

    while left <= right:
        
        mid : int = (left + right) // 2
        
        if mid**2 > N:
            right = mid - 1
        elif mid**2 < N:
            left = mid + 1
        else:
            return mid

N : int = int(input())
print(binary_search(N))