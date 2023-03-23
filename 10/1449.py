from typing import *
import sys

input = sys.stdin.readline

def solution(N : int , L : int) -> int:
    global arr

    count : int = 1
    start_location : int = arr[0]

    for location in arr[1:]:
        
        if location in range(start_location , start_location + L):
            continue
            
        else:
            start_location = location
            count += 1
    
    return count
N , L = map(int , input().split())
arr : List[int] = sorted(list(map(int , input().split())))
print(solution(N , L))