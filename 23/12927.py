from typing import *
import sys

input = sys.stdin.readline

switch = list(input().rstrip())

count : int = 0

for i in range(len(switch)):
    if switch[i] == 'Y':
        count += 1
        for j in range(i , len(switch) , i + 1):
            if switch[j] == 'Y':
                switch[j] = 'N'
            else:
                switch[j] = 'Y'
                
if 'Y' not in switch:
    print(count)
else:
    print(-1)