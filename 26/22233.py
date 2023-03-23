from typing import *
from collections import defaultdict
import sys

input =  sys.stdin.readline
data = defaultdict(str)

N , M = map(int , input().split())
for _ in range(N):
    keyword = input().rstrip()
    data[keyword] = 1

result : int = N
for _ in range(M):
    note = list(input().rstrip().split(','))
    for t in note:
        if t in data.keys():
            if data[t] == 1:
                data[t] -= 1
                result -= 1

    print(result)