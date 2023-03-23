from typing import *
import sys

input = sys.stdin.readline

N , M = map(int , input().split())
arr = list(map(int , input().split()))
prefix = [0]

summ : int = 0
for num in arr:
    summ += num
    prefix.append(summ)

# 투 포인터 알고리즘
start : int = 0
end : int = 0
count : int = 0

while start <= N and end <= N:
    
    if prefix[end] - prefix[start] == M:
        count += 1
        end += 1
    elif prefix[end] - prefix[start] < M:
        end += 1
    else:
        start += 1

print(count)