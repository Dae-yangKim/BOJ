from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
binn = list(bin(N)[2:])[::-1]

count , result = 1 , 0
for b in binn:
    result += int(b) * count
    count *= 3

print(result)