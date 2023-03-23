from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
dp = [0] * (N + 1)
dp[0] = 1

arr = [2 ** k for k in range(21)]

for i in arr:
    if i <= N:
        for j in range(i , N + 1):
            dp[j] += (dp[j - i])%1000000000

print(dp[N])