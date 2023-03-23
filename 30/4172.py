from typing import *
from math import *
import sys

input = sys.stdin.readline

dp = [1] * (1000001)

for i in range(1 , 1000001):
    dp[i] = (dp[floor(i - sqrt(i))] + dp[floor(log(i))] + dp[floor(i * sin(i) * sin(i))]) % 1000000

while True:
    i : int = int(input())
    if i == -1:
        break
    print(dp[i])