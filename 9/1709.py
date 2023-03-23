from typing import *
import sys

input = sys.stdin.readline

def solution(N : int) -> int:
    result : int = 0
    r : int = N // 2

    r_squared = r ** 2
    
    x : int = 0
    y : int = r - 1
    
    while True:
        if x == (r - 1) and y == 0: 
            result += 1
            break 

        if (x**2 + y**2) < r_squared and ((x + 1)**2 + (y + 1)**2) > r_squared:
            result += 1
            x += 1
        elif x**2 + y**2 == r_squared:
            y -= 1
        else:
            x -= 1
            y -= 1

    return result * 4

N : int = int(input())
print(solution(N))