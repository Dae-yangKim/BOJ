from typing import *
import sys

input = sys.stdin.readline

N : int = int(input()) # 토핑의 개수
A , B = map(int , input().split()) # 도우의 가격 , 토핑의 가격
C : int = int(input()) # 도우의 열량
kcal_arr = []
for _ in range(N):
    kcal_arr.append(int(input()))
kcal_arr = sorted(kcal_arr , reverse = True)

result : int = C / A

for i in range(1 , len(kcal_arr) + 1):
    
    kcal : int = C + sum(kcal_arr[0 : i])
    price : int = A + (B * i)
    
    if kcal / price > result:
        result = kcal / price
    else:
        break

print(int(result))