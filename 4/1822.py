from typing import *
import sys

input = sys.stdin.readline

N , M = map(int , input().split())

set_1 = set(map(int , input().split()))
set_2 = set(map(int , input().split()))

result_set = list(set_1.difference(set_2))
len_set = len(result_set)

if len_set == 0:
    print(0)
else:
    print(len(result_set))
    result_set = sorted(result_set)
    for i in result_set:
        print(i , end = ' ')    