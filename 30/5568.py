from typing import *
import itertools
import sys

input = sys.stdin.readline

N : int = int(input())
K : int = int(input())

card = [input().rstrip() for _ in range(N)]
data = set("".join(i) for i in itertools.permutations(card , K))
print(len(data))