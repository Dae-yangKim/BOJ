from typing import *
import re
import sys

input = sys.stdin.readline

N : int = int(input())
serial = [input().rstrip() for _ in range(N)]

serial = sorted(serial , key = lambda x : (len(x) , sum(list(map(int , re.findall(r'\d' , x)))) , x))

for sub in serial:
    print(sub)