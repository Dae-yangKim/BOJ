from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
tree = list(map(int , input().split()))
growth = list(map(int , input().split()))

sorted_list = sorted(zip(tree , growth) , key = lambda x : x[1])

tree_sorted , growth_sorted = zip(*sorted_list)

result : int = 0
for idx in range(len(tree_sorted)):
    result += tree_sorted[idx] + (growth_sorted[idx] * idx)

print(result)