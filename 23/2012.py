from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
rank = []
for _ in range(N):
    rank.append(int(input()))
rank = sorted(rank)

result = 0
for i in range(N):
    result += abs(rank[i] - (i + 1))

print(result)