from typing import *
import sys

input = sys.stdin.readline

def gcd(i : int , j : int):
    
    if j == 0:
        return i
    return gcd(j , i % j)

dp : List[int] = [0 for _ in range(1001)]
dp[1] = 3

for i in range(2 , 1001):
    count : int = 0

    for j in range(1 , i + 1):
        if i == j:
            continue

        if gcd(i , j) == 1:
            count += 2
    
    dp[i] = dp[i - 1] + count

N : int = int(input())

for _ in range(N):
    n : int = int(input())

    print(dp[n])