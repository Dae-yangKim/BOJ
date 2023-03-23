from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
arr : List[int] = []
for i in range(N):
    plug : int = int(input())
    arr.append(plug)

sum_value : int = 0
for i in range(len(arr) - 1):
    arr[i] -= 1

print(sum(arr))