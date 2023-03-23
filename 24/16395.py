from typing import *
import sys

input = sys.stdin.readline

n , k = map(int , input().split())

if n == 1 or n == 2:
    print(1)
else:
    dp = [[] for _ in range(n + 1)]

    dp[1] = [1]
    dp[2] = [1 , 1]

    for i in range(3 , n + 1):    
        dp[i].append(1)
        for j in range(1 , i - 1):
            dp[i].append(dp[i - 1][j - 1] + dp[i - 1][j])
        dp[i].append(1)

    print(dp[n][k - 1])