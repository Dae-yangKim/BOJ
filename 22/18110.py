from typing import *
import sys

input = sys.stdin.readline

n : int = int(input())

if n == 0:
    print(0)
else:
    arr : List[int] = []

    for _ in range(n):
        arr.append(int(input()))

    arr = sorted(arr)
    percent = round((n * 0.15) + 0.0000001)

    summ : int = sum(arr[percent : len(arr) - percent])
    count : int = len(arr[percent : len(arr) - percent])

    print(round((summ / count) + 0.0000001))