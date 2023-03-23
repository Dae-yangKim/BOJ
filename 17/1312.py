from typing import *
import sys

input = sys.stdin.readline

def solution(a : int , b : int , n : int) -> int:

    result = str(a / b).split('.')

    if len(result[1]) < n:
        return 0

    return result[1][n - 1]

a , b , n = map(int , input().split())
print(solution(a , b , n))