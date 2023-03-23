from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
arr : List[int] = []

for _ in range(N):
    num : float = float(input())
    arr.append(num)

arr = sorted(arr)

for num in arr[:7]:
    print("{:.3f}".format(num))