from typing import *
import sys

input = sys.stdin.readline

N , M = map(int , input().split())
graph = []
row , col = 0 , 0

for i in range(N):
    graph.append(list(input().rstrip()))

for a in range(N):
    if "X" not in graph[a]:
        row += 1

for b in range(M):
    if "X" not in [graph[i][b] for i in range(N)]:
        col += 1

print(max(row , col))