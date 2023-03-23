from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
arr : List[int] = sorted(map(int , input().split()) , reverse = True)

result : int = 0

for i in range(N):
    result += 2 * (N - 1 - 2 * i) * arr[i]

print(result)