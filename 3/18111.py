from typing import *
import sys

input = sys.stdin.readline

def solution(N , M , B , block_map) -> int:
    pass

N , M , B = map(int , input().split())
block_map : List[int] = []

for i in range(N):
    block : List[int] = list(map(int , input().split()))
    block_map.append(block)

print(solution(N , M , B , block_map))