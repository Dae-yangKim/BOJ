from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
arr = list(map(int , input().split()))
profit , result = 0 , 0

for i in range(N - 1 , -1 , -1):
    profit : int = max(profit , arr[i])
    result : int = max(result , profit - arr[i])

print(result)