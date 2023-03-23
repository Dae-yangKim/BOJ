from typing import *
import sys

input = sys.stdin.readline

N , M = map(int , input().split())
p_arr : List[int] = []
for _ in range(M):
    p_arr.append(int(input()))

p_arr = sorted(p_arr)

price_arr : List[int] = []

for i in range(1 , p_arr[-1] + 1):
    count : int = 0
    for j in range(len(p_arr)):
        if i <= p_arr[j]:
            count += 1
    price_arr.append(i * count)

result : int = max(price_arr)
idx : int = price_arr.index(max(price_arr)) + 1

print(f"{idx} {result}")