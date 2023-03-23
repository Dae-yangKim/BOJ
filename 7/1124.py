from typing import *
import sys
import math

input = sys.stdin.readline
n : int = 100000

table = [True for _ in range(n + 1)]
table[1] = False

m = int(math.sqrt(n))
for i in range(2 , m+1):
    if table[i]:
        for j in range(i + i , n + 1 , i):
            table[j] = False

A , B = map(int , input().split())
arr : List[int] = list(range(A , B+1))

dp : List[int] = [0] * (B+1)
for i in range(1 , B+1):
    if table[i]:
        dp[i] = 1
for i in range(2 , B+1):
    for j in range(2 , B+1):
        if i * j > B:
            break
        if table[j]:
            dp[i * j] = dp[i] + 1

result : int= 0 
for i in range(A , B+1):
    if table[dp[i]]:
        result += 1
print(result)