from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())

start , end = 0 , 0
count , summ = 0 , 0

while end <= N:
    
    if summ < N:
        end += 1
        summ += end
    elif summ > N:
        summ -= start
        start += 1
    else:
        count += 1
        end += 1
        summ += end
    
print(count)