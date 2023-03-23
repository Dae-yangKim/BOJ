from typing import *
import sys

input = sys.stdin.read

# DP
dp = {}
def solution(N : int) -> int:
    global dp

    if N in dp.keys():
        return dp[N]
    elif N <= 1:
        return 1
    else:
        dp[N] = N * solution(N - 1)
        return dp[N]

N : int = int(input())
print(solution(N))