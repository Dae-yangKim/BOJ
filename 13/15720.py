from typing import *
import sys

input = sys.stdin.readline

B , C , D = map(int , input().split())
arr : List[int] = []

for i in range(3):
    menu : List[int] = list(map(int , input().split()))
    arr.append(menu)

length = min(len(arr[0]) , min(len(arr[1]) , len(arr[2])))
sum_result = sum(arr[0]) + sum(arr[1]) + sum(arr[2])
discount = 0

for i in range(length):
    
    discount += (max(arr[0]) + max(arr[1]) + max(arr[2])) * 0.1

    arr[0].pop(arr[0].index(max(arr[0])))
    arr[1].pop(arr[1].index(max(arr[1])))
    arr[2].pop(arr[2].index(max(arr[2])))

print(sum_result)
print(int(sum_result - discount))