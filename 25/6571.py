from typing import *
import sys

input = sys.stdin.readline

dp = [1 , 1]
idx = 1

while dp[-1] < 10**100:
    dp.append(dp[idx] + dp[idx - 1])
    idx += 1

while True:
    a , b = map(int , input().split())

    if a == 0 and b == 0:
        break
    
    result_a , result_b = 0 , 0
    
    for i in range(len(dp)):
        if dp[i] >= a and result_a == 0:
            result_a = i
        
        if dp[i] >= b and result_b == 0:
            result_b = i
        
    print(result_b - result_a)