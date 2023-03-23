from typing import *
import sys

input = sys.stdin.readline

N : str = input().strip()
condition : bool = False

for i in range(1 , len(N)):
    
    value_1 : int = 1
    value_2 : int = 1

    for j in N[:i]:
        value_1 *= int(j)
    
    for k in N[i:]:
        value_2 *= int(k)
    
    if value_1 == value_2:
        condition = True
        print("YES")
        break
    else:
        continue

if not condition:
    print("NO")