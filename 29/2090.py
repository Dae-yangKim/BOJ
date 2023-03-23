from typing import *
import sys

input = sys.stdin.readline

def lcm(a : int , b : int) -> int:
    return (a * b) // gcd(a , b)

def gcd(a : int , b : int) -> int:
    while b != 0:
        a , b = b , (a % b)
    return a

N : int = int(input())
arr = list(map(int , input().split()))

l : int = arr[0]
for i in range(1 , len(arr)):
    l = lcm(l , arr[i])

result : int = 0
for i in arr:
    result += (l // i)

print(f"{l}/{result}")