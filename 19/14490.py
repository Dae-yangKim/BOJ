from typing import *
import sys

input = sys.stdin.readline

def gcb(a , b):

    tmp : int = a % b

    while tmp != 0:
        a = b
        b = tmp
        tmp = a % b
    
    return abs(b)

arr = list(input().rstrip().split(":"))
arr[0] = int(arr[0])
arr[1] = int(arr[1])

num : int = gcb(arr[0] , arr[1])

print(f"{arr[0] // num}:{arr[1] // num}")