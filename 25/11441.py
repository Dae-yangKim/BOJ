from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
arr : List[int] = list(map(int , input().split()))
prefix_sum = [0] * (N+1)
for i in range(1 , N+1):
    prefix_sum[i] = arr[i - 1] + prefix_sum[i - 1]

M : int = int(input())
for i in range(M):
    a , b = map(int , input().split())
    print(prefix_sum[b] - prefix_sum[a - 1])