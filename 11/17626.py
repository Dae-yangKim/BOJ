from typing import *
import sys

input = sys.stdin.readline

n : int = int(input())
dp : List[int] = [0 , 1]

for i in range(2 , n + 1):
    
    minimum = 1e9
    idx = 1

    while idx**2 <= i:

        minimum = min(minimum , dp[i - (idx ** 2)])

        idx += 1
    
    dp.append(minimum + 1)

print(dp[n])