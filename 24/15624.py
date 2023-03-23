from typing import *
import sys

input = sys.stdin.readline

n : int = int(input())
dp_1 , dp_2 = 0 , 1

for i in range(2 , n + 1):
    dp_1 , dp_2 = (dp_1 + dp_2)%1000000007 , dp_1%1000000007

print(dp_1 % 1000000007)