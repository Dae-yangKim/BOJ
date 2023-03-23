from typing import *
import sys

input = sys.stdin.readline

def gcd(m,n):
    while n != 0:
       t = m%n
       (m,n) = (n,t)
    return abs(m)

R , G = map(int , input().split())
ma : int = gcd(R , G)

for i in range(1 , ma+1):
    if R % i == 0 and G % i == 0:
        print("{} {} {}".format(i , R // i ,G // i))