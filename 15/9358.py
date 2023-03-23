from typing import *
import sys

input = sys.stdin.readline

def solution(arr : List[int]) -> bool:

    while len(arr) != 2:
        
        length : int = (len(arr) // 2) + 1
        
        for i in range(length):
        
            value : int = arr[i] + arr[-(i + 1)]

            arr[i] = value
        
        del arr[length :]
    
    if arr[0] > arr[1]:
        return True
    else:
        return False

    
N : int = int(input())
for _ in range(N):
    
    n : int = int(input())
    arr : List[int] = list(map(int , input().split()))
    
    if solution(arr):
        print("Case #1: Alice")
    else:
        print("Case #2: Bob")