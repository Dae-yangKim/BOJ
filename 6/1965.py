from typing import *
import sys

input = sys.stdin.readline

def solution(arr : List[int]) -> None:
    for i in range(num):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i] , dp[j] + 1)

num : int = int(input())
arr : List[int] = list(map(int , input().split()))
dp : List[int] = [1 for _ in range(num)]

solution(arr)
print(dp)
print(max(dp))