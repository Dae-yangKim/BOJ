from typing import *
import sys

input = sys.stdin.readline

a , k = map(int , input().split())

count = 0

while True:
    if a == k:
        print(count)
        break
    elif k % 2 == 0 and k >= a * 2:
        k = int(k / 2)
    else:
        k -= 1

    count += 1