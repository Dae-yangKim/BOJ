from typing import *
import sys

input = sys.stdin.readline

cache = {}

def factorial(n : int) -> int:
    global cache

    if n in cache:
        return cache[n]
    elif n <= 1:
        return 1
    else:
        cache[n] = n * factorial(n - 1)
        return cache[n]

n , m = map(int , input().split())

f : int = 1
for i in range(m):
    f = f * (n - i)

print(f // factorial(m))