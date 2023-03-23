from typing import *
import sys

input = sys.stdin.readline

def solution(num):
    zeros = 0

    while num >= 5:
        
        zeros += num // 5
        num //= 5
    
    return zeros

num : int = int(input())
left , right , result = 1 , num * 5 , 0

while left <= right:
    
    mid = (left + right) // 2
    
    zero = solution(mid)

    if zero < num:
        left = mid + 1
    
    else:
        right = mid - 1
        result = mid

print(result if solution(result) == num else -1)