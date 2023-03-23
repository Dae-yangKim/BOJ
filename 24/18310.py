from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
house : List[int] = list(map(int , input().split()))

house = sorted(house)
length : int = len(house)

if length % 2 == 0:
    print(house[(length - 1) // 2])
else:
    print(house[length // 2])