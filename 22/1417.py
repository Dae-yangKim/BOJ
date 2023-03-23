from typing import *
import sys

input = sys.stdin.readline

n : int = int(input())
target : int = int(input())
arr : List[int] = []

for _ in range(n - 1):
    arr.append(int(input()))

count : int = 0
arr = sorted(arr , reverse = True)

if n == 1:

    print(0)
else:

    while arr[0] >= target:
        count += 1
        target += 1
        arr[0] -= 1
        arr = sorted(arr , reverse = True)

    print(count)