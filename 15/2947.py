from typing import *
import sys

input = sys.stdin.readline

arr = list(map(int , input().split()))

while True:

    if arr == sorted(arr):
        break

    for idx in range(len(arr) - 1):

        if arr[idx] > arr[idx + 1]:
            arr[idx] , arr[idx + 1] = arr[idx + 1] , arr[idx]
            print(' '.join(str(element) for element in arr))