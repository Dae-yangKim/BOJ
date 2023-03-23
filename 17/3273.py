from typing import *
import sys

input = sys.stdin.readline

def binary_search(arr : List[int] , X : int) -> int:

    left : int = 0
    right : int = len(arr) - 1

    count : int = 0
    
    while left < right:

        if arr[left] + arr[right] == X:
            count += 1
        if arr[left] + arr[right] < X:
            left += 1
        else:
            right -= 1
    
    return count

N : int = int(input())
arr : List[int] = list(map(int , input().split()))
X : int = int(input())

print(binary_search(sorted(arr) , X))