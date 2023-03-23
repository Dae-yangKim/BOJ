from typing import *
from collections import defaultdict
import sys

input = sys.stdin.readline

N , C = map(int , input().split())
data = defaultdict(int)

arr = list(map(int , input().split()))

for num in arr:
    data[num] += 1

data = sorted(data.items() , key = lambda x : x[1] , reverse = True)

for tp in data:
    for _ in range(tp[1]):
        print(tp[0] , end = ' ')