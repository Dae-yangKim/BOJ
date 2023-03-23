from typing import *
import sys

input = sys.stdin.readline

N , M = map(int , input().split())
arr = sorted(list(map(int , input().split())))

summ : int = 0
prefix = [0]
for num in arr:
    summ += num
    prefix.append(summ)

for _ in range(M):
    L , R = map(int , input().split())
    print(prefix[R] - prefix[L - 1])