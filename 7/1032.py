from typing import *
import sys

input = sys.stdin.readline

def solution(pattern_arr : List[List[str]]) -> str:
    first_pattern : List[str] = pattern_arr[0]
    
    for i in pattern_arr[1 :]:
        for j in range(len(i)):
            if first_pattern[j] != i[j]:
                first_pattern[j] = "?"
    
    pattern_result : str = "".join(first_pattern)
    return pattern_result

N : int = int(input())
pattern_arr : List[List[str]] = []
for i in range(N):
    pattern : List[str] = list(input()) ; pattern_arr.append(pattern)
pattern_result : str = solution(pattern_arr)
print(pattern_result)