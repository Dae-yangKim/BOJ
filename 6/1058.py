from typing import *
import sys

input = sys.stdin.readline

def solution(arr : List[List[str]]) -> None:
    global connected
    
    for k in range(num):
        for i in range(num):
            for j in range(num):
                if i == j: continue
                
                if arr[i][j] == "Y" or (arr[i][k] == "Y" and arr[k][j] == "Y"):
                    connected[i][j] = 1
num : int = int(input())
arr : List[List[str]] = [list(input()) for _ in range(num)]
connected = [[0] * num for _ in range(num)]

solution(arr)

answer : int = 0
for row in connected:
    answer = max(answer , sum(row))
print(answer)