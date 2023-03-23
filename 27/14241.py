from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
arr = list(map(int , input().split()))
slime : int = arr[0]
score : int = 0

for i in range(1 , len(arr)):
    score += slime * arr[i]
    slime += arr[i]

print(score)