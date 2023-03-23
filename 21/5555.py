from typing import *
import sys 

input = sys.stdin.readline

sentence : str = input().rstrip()
N : int = int(input())
count : int = 0

for i in range(N):
    
    ring : str = input().rstrip()

    if sentence in ring * 2:
        count += 1

print(count)