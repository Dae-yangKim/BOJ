from typing import *
import sys

input = sys.stdin.readline

subject : List[int] = [0] * 6

for i in range(6):
    subject[i] = int(input())

science : List[int] = sorted(subject[:4] , reverse=True)
history : List[int] = sorted(subject[4:] , reverse=True)

result : int = sum(science[:3]) + history[0]

print(result)