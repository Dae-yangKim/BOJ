from typing import *
import sys

input = sys.stdin.readline

def factorial(n : int) -> int:
    f : int = 1
    for i in range(1 , n + 1):
        f = f * i
    return f
def solution(n : int) -> int:
    result : int = 0
    for i in range((n // 2) + 1):
        result += (factorial(n - i) // (factorial(i) * factorial(n - 2 * i))) * (2 ** i)
    return result                    

while True:
    try:
        n : int = int(input())
        print(solution(n))
    except:
        break