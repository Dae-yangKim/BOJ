from typing import *
import sys

input = sys.stdin.readline

T : int = int(input())
dp : List[int] = [0] * 10001
dp[1] = 1
dp[2] = 1

for idx in range(3 , 10001):
    dp[idx] = dp[idx - 2] + dp[idx - 1]

for i in range(1 , T + 1):
    P , Q = map(int , input().split())
    print("Case #{}: {}".format(i ,dp[P] % Q))