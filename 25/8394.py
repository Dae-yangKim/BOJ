from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())

if N == 1:
    print(0)
elif N < 3:
    print(N)
else:
    dp = [0] * (N + 1)
    dp[2] = 2
    dp[3] = 3

    for i in range(4 , N + 1):
        dp[i] = int(str(dp[i - 1] + dp[i - 2])[-1])

    print(dp[N])