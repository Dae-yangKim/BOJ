from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())

for _ in range(N):
    G : int = int(input())

    arr : List[int] = [0] * G
    test_arr : List[int] = [0] * G
    min_num : int = 1

    for idx in range(G):
        arr[idx] = int(input())
    
    if G == 1:
        print(1)
        continue

    while True:

        for i in range(len(arr)):
            test_arr[i] = arr[i] % min_num
            
        if len(set(test_arr)) == G:
            print(min_num)
            break
            
        else:
            min_num += 1
            continue