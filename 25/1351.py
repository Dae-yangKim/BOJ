from typing import *
import sys
import collections

input = sys.stdin.readline

def calculation(i , p , q):
    if dp[i] != 0:
        return dp[i]
    dp[i] = (calculation(int(i / p) , p , q) + calculation(int(i / q) , p , q))
    return dp[i]

N , P , Q = map(int , input().split())
dp = collections.defaultdict(int)
dp[0] = 1

print(calculation(N , P , Q))