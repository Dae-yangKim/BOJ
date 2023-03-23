from typing import *
import sys

input = sys.stdin.readline

def solution(num : int) -> int:
    global dp , result
    
    if dp[num] != 0:
        return dp[num]

    for i in range(4 , num + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
    return dp[num]

T : int = int(input())
result : int = 0
dp : List[int] = [0] * 12
dp[1] = 1 ; dp[2] = 2 ;dp[3] = 4
for i in range(T):
    num : int = int(input())
    print(solution(num))
    result = 0