from typing import *
import sys

input = sys.stdin.readline

def solution(arr : List[int] , L : int) -> int:
    
    length : int = L

    while True:
        check_len = length
        
        for idx in range(len(arr)):
            
            if length >= arr[idx]:
                length += 1
                arr.pop(idx)
                break
    
        if length == check_len:
            break
        else:
            continue
    
    return length
    
N , L = map(int , input().split())
arr = list(map(int , input().split()))

print(solution(arr , L))