from typing import *
import sys

input = sys.stdin.readline

A , P = map(int , input().split())

nums = [A]
while True:
    temp = 0
    for i in str(nums[-1]):
        temp += int(i) ** P
    
    if temp in nums:
        break

    nums.append(temp)

print(nums.index(temp))