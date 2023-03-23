from typing import *
import sys

input = sys.stdin.readline

R , C , W = map(int , input().split())

length : int = (R + W) - 1
dp = [0 , [1] , [1 , 1]]

for i in range(3 , length + 1):
    dp.append([1])
    for j in range(1 , i - 1):
        dp[i].append(dp[i - 1][j - 1] + dp[i - 1][j])
    dp[i].append(1)


result : int = 0
idx : int = C - 1
for i in range(R , length + 1):
    result += sum(dp[i][idx : C])
    C += 1

print(result)