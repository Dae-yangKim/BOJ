from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
dp = [0 for _ in range(N + 1)]

t = [] ; p = []

for _ in range(N):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)


for i in range(N-1, -1, -1): 
    if t[i] + i > N: 
        dp[i] = dp[i+1] 
    
    else:
        dp[i] = max(dp[i+1], dp[t[i] + i] + p[i]) 

print(dp)