from typing import *
import sys

input = sys.stdin.readline


N : int = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))

arr = sorted(arr , reverse = True)

result_arr = []

for idx in range(len(arr)):
    result_arr.append(arr[idx] * (idx + 1))

print(max(result_arr))