from typing import *
import sys

input = sys.stdin.readline

def gcd(a , b) -> int: #최대공약수
    while b != 0:
        a , b = b , a % b
    
    return a

def lcm(a , b) -> int: #최소공배수
    return (a * b) // gcd(a , b)

N : int = int(input())
for _ in range(N):
    
    a , b = map(int , input().split())

    print(lcm(a , b) , gcd(a , b))