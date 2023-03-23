from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
arr : List[str] = []

for i in range(N):
    
    arr.append(input())

arr_set = list(set(arr))

maximum : int = arr.count(arr_set[0])
result : str = arr_set[0]

for i in arr_set[1:]:
    
    if maximum < arr.count(i):
        
        maximum = arr.count(i)
        result = i
    
    elif maximum == arr.count(i):
        
        if result > i:
    
            result = i

print(result)