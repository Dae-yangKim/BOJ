from typing import *
from collections import defaultdict
import sys

input = sys.stdin.readline

N : int = int(input())
data_1 = defaultdict(list)
data_2 = defaultdict(list)

for _ in range(N):
    x , y = map(int , input().split())
    data_1[x].append(y)
    data_2[y].append(x)

count : int = 0
for key in data_1:
    if len(data_1[key]) >= 2:
        count += 1
for key in data_2:
    if len(data_2[key]) >= 2:
        count += 1
print(count)