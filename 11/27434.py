from typing import *
import sys

input = sys.stdin.readline

def factorial(n : int) -> int:
    
    result : int = 1

    for i in range(n , 0 , -1):
        result *= i
    
    return result

N : int = int(input())
print(factorial(N))