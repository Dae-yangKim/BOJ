from typing import *
import collections
import sys

input = sys.stdin.readline

def calculation(i , p , q):
    if i <= 0:
        return 1

    if dp[i] != 0:
        return dp[i]
    dp[i] = (calculation(int(i / p) - X , p , q) + calculation(int(i / q) - Y , p , q))
    return dp[i]

N , P , Q , X , Y = map(int , input().split())
dp = collections.defaultdict(int)
dp[0] = 1

print(calculation(N , P , Q))