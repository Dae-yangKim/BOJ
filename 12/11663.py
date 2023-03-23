from typing import *
import sys

input = sys.stdin.readline

def binary_search(point_1 : int , point_2 : int , left : int , right : int) -> int:
    global point

    value : int = point[len(point) // 2]
    
    
N , M = map(int , input().split()) # 개수
point : List[int] = list(map(int , input().split())) # 좌표

for i in range(M):
    point_1 , point_2 = map(int , input().split())
    print(binary_search(point_1 , point_2))