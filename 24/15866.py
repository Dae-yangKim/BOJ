from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
graph = list(input().rstrip())

present : int = 0
for idx in range(N - 1):
    if graph[idx] == 'E' and graph[idx + 1] == 'W':
        present += 1

print(present)
