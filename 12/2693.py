from typing import *
import sys

input = sys.stdin.readline

T : int = int(input())
N : int = 3

for i in range(T):
    arr : List[int] = sorted(list(map(int , input().split())) , reverse=True)
    print(arr[N - 1])