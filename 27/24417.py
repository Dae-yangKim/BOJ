from typing import *
import sys

input = sys.stdin.readline

n : int = int(input())
num : int = 1000000007
x = 1 ; y = 1
count : int = n - 2
for i in range(n - 2):
    #a , b = b , (a+b)%num
    y , x = (x + y)%num , y
print(y , count)