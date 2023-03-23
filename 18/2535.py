from typing import *
import sys

input = sys.stdin.readline

data = []

N : int = int(input())
for _ in range(N):
    
    country , student , score = map(int , input().split())

    data.append((country , student , score))

data = sorted(data , key = lambda x : x[2] , reverse=True)

check = []
result = []
for value in data:

    if len(result) == 3:
        break
    
    if check.count(value[0]) < 2:
        check.append(value[0])
        result.append(value)
    else:
        continue

for idx in range(3):
    print(result[idx][0] , result[idx][1])