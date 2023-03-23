from typing import *
import sys

input = sys.stdin.readline

def solution(N : int) -> int:
    global dp

    if dp[N] != 0:
        return dp[N]

    result : int = 0
    for i in range(N):
        result += solution(i) * solution(N - (i + 1))

    dp[N] = result
    return dp[N]
    
N : int = int(input())
dp : List[int] = [0] * (N + 1)
dp[0] = 1
print(solution(N))