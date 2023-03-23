from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
count : int = 0

while True:

    if N % 5 == 0:
        count += N // 5
        break
    else:
        N -= 2
        count += 1
    
    if N < 0:
        break

if N < 0:
    print(-1)
else:
    print(count)