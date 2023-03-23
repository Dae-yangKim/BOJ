from typing import *
import sys

input = sys.stdin.readline

def Rev(x : str) -> int:
    return int("".join(reversed(x)))

x1 , x2 = map(str , input().split())
print(Rev(str(Rev(x1) + Rev(x2))))