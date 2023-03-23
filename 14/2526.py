from typing import *
import sys

input = sys.stdin.readline

N , P = map(int , input().split())
num : int = N
arr = []

while True:

    value : int = (num * N) % P
    
    if value not in arr:
        
        arr.append(value)
        
        num : int = value

    else:

        idx = arr.index(value)

        print(len(set(arr[idx :])))
        
        break