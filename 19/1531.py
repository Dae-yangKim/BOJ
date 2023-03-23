from typing import *
import sys

input = sys.stdin.readline

N , M = map(int , input().split())
graph = [[0] * 100 for _ in range(100)]

for _ in range(N):
    
    x1 , y1 , x2 , y2 = map(int , input().split())
    
    for x in range(x1 , x2 + 1):
        
        for y in range(y1 , y2 + 1):
            
            graph[x - 1][y - 1] += 1

count : int = 0

for x in range(100):
    
    for y in range(100):

        if graph[x][y] > M:
            count += 1

print(count)