from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
A = [list(map(int , input().split())) for _ in range(N)]
B = [list(map(int , input().split())) for _ in range(N)]

count : int = 0

for i in range(N):
    for j in range(N):
        for k in range(N):

            if A[i][k] and B[k][j]:
                count += 1
                break

print(count)