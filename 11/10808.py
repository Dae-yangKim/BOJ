from typing import *
import sys

input = sys.stdin.readline

arr : List[int] = [0] * (ord("z") - ord("a") + 1)
standard_number = ord("a")

sentence : str = list(input().strip())

for element in sentence:
    arr[ord(element) - standard_number] += 1

for element in arr:
    print(element , end = ' ')