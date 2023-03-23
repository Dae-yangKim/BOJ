from typing import *
import sys

input = sys.stdin.readline

A , B = map(int , input().split())
N : int = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))

arr = sorted(arr , reverse = True)

min_result = min(abs(arr[0] - B) + 1 , abs(A - B))

for idx in range(1 , len(arr)):

    result : int = min(abs(arr[idx] - B) + 1 , abs(A - B))

    if result < min_result:
        min_result = result

print(min_result)