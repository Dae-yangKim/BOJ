from typing import *
import sys

input = sys.stdin.readline

data = dict()

N : int = int(input())

for i in range(N):

    element = input().split(".")[1].strip()

    if element not in data:
        
        data[element] = 1
    else:
        
        data[element] += 1

data = sorted(data.items())

for value in data:
    print(value[0] , value[1])
    