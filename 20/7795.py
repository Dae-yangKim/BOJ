from typing import *
import sys

input = sys.stdin.readline

def binary_search(arr , a):
    left , right = 0 , len(arr) - 1
    count = -1

    while left <= right:

        middle = (left + right) // 2

        if arr[middle] < a:
            count = middle
            left = middle + 1
        else:
            right = middle - 1
    
    return count    
    
for _ in range(int(input())):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    count = 0

    for a in A:
        count += (binary_search(B, a) + 1)
    
    print(count)