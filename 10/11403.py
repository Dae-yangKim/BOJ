from typing import *
import sys

input = sys.stdin.readline


num = int(input())
arr = [0] * num

for i in range(num):
    arr[i] = list(map(int , input().split()))

# 플로이드 워셜 알고리즘
for k in range(num):
    for x in range(num):
        for y in range(num):
            
            if arr[x][y] == 1 or (arr[x][k] == 1 and arr[k][y] == 1):
                arr[x][y] = 1

for i in arr:
    for j in i:
        print(j , end = " ")
    print()