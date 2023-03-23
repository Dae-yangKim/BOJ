from typing import *
import sys

input = sys.stdin.readline

def solution(arr : List[List[int]]) -> int:
    length_arr : List[int] = []

    for i in range(3):
        for j in range(i + 1 , 4):
            length_arr.append((arr[i][0] - arr[j][0])**2 + (arr[i][1] - arr[j][1])**2)
    
    length_arr.sort()
    
    if length_arr[0] == length_arr[1] and length_arr[0] == length_arr[2] and length_arr[0] == length_arr[3] and \
        length_arr[4] == length_arr[5]:
        return 1
    else:
        return 0
    
num : int = int(input())

for i in range(num):
    arr : List[List[int]] = [list(map(int, input().split())) for _ in range(4)]
    result = solution(arr)
    print(result)