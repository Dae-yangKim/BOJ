from typing import *
import sys

input = sys.stdin.readline

arr : List[int] = sorted(list(map(int , input().split())))

a : int = min(arr)
d : int = min(abs(arr[0] - arr[1]) , abs(arr[1] - arr[2]))

s : int = 2 * (2 * a + 3 * d)

print(abs(s - sum(arr)))