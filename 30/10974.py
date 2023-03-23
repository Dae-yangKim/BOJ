from typing import *
from itertools import permutations
import sys

input = sys.stdin.readline

N : int = int(input())
nums = [i for i in range(1 , N +  1)]

arr = [i for i in permutations(nums , N)]
for sets in arr:
    print(" ".join(map(str , sets)))