from typing import *
import sys

input = sys.stdin.readline

def solution(arr : List[int]) -> int:

    count : int = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1 , len(arr)):
            
            if arr[i] > arr[j]:
                arr[i] , arr[j] = arr[j] , arr[i]
                count += 1
    
    return count
T : int = int(input())
for _ in range(T):
    usr_input = list(map(int , input().split()))
    test_number , arr = usr_input[0] , usr_input[1 : ]
    
    print(f"{test_number} {solution(arr)}")