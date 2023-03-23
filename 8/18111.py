from typing import *
import sys

input = sys.stdin.readline

N , M , B = map(int , input().split())
blocks : List[List[int]] = [list(map(int , input().split())) for _ in range(N)]
result = sys.maxsize
idx : int = 0

for floor in range(257):
    max_size , min_size = 0 , 0

    for row in range(N):
        for col in range(M):
            if blocks[row][col] >= floor:
                max_size += blocks[row][col] - floor
            else:
                min_size += floor - blocks[row][col]
    
    if max_size + B >= min_size:
        if min_size + (max_size * 2) <= result:
            result = min_size + (max_size * 2)
            idx = floor

print(result , idx)