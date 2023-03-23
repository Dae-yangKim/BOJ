from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
data = []

for _ in range(N):
    arr = list(map(str , input().split()))
    data.append(arr)

data.sort(key = lambda x : x[1] , reverse = True)
data.sort(key = lambda x : x[0])

for arr in data:
    
    print(f"{arr[0]} {arr[1]}")