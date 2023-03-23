from typing import *
import sys

input = sys.stdin.readline

arr : List[int] = []

def dfs(row , col , arr) -> int:
    
    for row_idx in range(row):

        for col_idx in range(col):

            if arr[row_idx][col_idx] == 1:
                

while True:
    
    col , row = map(int , input().split())

    for _ in range(row):
        sub = list(map(int , input().split()))
        arr.append(sub)
    
    print(dfs(row , col , arr))