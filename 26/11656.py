from typing import *
import sys

input = sys.stdin.readline

sentence = input().rstrip()
arr = []

for i in range(len(sentence)):
    arr.append(sentence[i:])

arr = sorted(arr)
for sub in arr:
    print(sub)