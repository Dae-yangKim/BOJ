from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
num = 1000000009

dp = []
dp.append(1)
dp.append(1)
dp.append(2)

for i in range(3 , 1000001):
    dp.append((dp[i - 1] + dp[i - 2] + dp[i - 3]) % num)

for _ in range(N):
    n = int(input())
    print(dp[n])