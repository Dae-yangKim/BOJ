from typing import *
import sys

input = sys.stdin.readline

def solution(K : int) -> tuple:
    num : int = 1

    while True:
        if num >= K:
            break
        num = num * 2
    
    min_num : int = num
    count : int = 0
    
    while True:

            if K % num == 0:
                break

            num = num // 2
            count += 1
        
    return (min_num , count)
K : int = int(input())
result : tuple = solution(K)
print(result[0] , result[1])