from typing import *
from collections import defaultdict
import sys

input = sys.stdin.readline

data = defaultdict(int)

N , M = map(int , input().split())

for _ in range(N):
    
    group_name = input().rstrip()
    data[group_name] = []
    num : int = int(input())

    for _ in range(num):
        data[group_name].append(input().rstrip())


for _ in range(M):

    usrInput = input().rstrip()
    num : int = int(input())

    if num == 1:
        for key in data.keys():
            if usrInput in data[key]:
                print(key)
                break
    else:
        for name in sorted(data[usrInput]):
            print(name)