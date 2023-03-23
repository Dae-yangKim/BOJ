from typing import *
import sys
input = sys.stdin.readline

def fib_dp(N) -> int:
    global zero_count , one_count , dp
    if dp[N] == None:
            
        if N == 1:
            one_count += 1
        elif N == 0:
            zero_count += 1

        if N < 2:
            dp[N] = N
        else:
            dp[N] = fib_dp(N-1) + fib_dp(N-2)
    
    return dp[N]
        
num : int = int(input())

for i in range(num):
    N : int = int(input())
    dp : List[int] = [None] * (N+1)
    zero_count : int = 0
    one_count : int = 0
    fib_dp(N)
    print(zero_count , one_count)