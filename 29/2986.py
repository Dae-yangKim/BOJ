from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
divisor = []

for i in range(1 , int(N ** (1 / 2)) + 1):
    if N % i == 0:
        divisor.append(i)
        if ((i ** 2) != N):
            divisor.append(N // i)

    divisor.sort()

if len(divisor) == 1:
    print(N - divisor[0])
else:
    print(N - divisor[-2])