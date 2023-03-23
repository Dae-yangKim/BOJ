from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    print(2 * N - 2)