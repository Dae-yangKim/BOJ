from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
arr = list(map(int , input().split()))
arr = sorted(arr , reverse=True)

result : int = 0
for idx in range(1 , len(arr)):
    result += (arr[0] + arr[idx])

print(result)