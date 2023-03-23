from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())

first_arr = list(map(int , input().split()))
second_arr = list(map(int , input().split()))

for idx in range(len(first_arr)):

    if first_arr[idx] < 0:
        first_arr[idx] = -first_arr[idx]
    
    if second_arr[idx] < 0:
        second_arr[idx] = -second_arr[idx]
    
print(sum(first_arr) + sum(second_arr))