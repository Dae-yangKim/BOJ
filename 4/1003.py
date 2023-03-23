from typing import *
import sys

input = sys.stdin.readline

def solution(N : int) -> tuple:

    if N == 0:
        return (1 , 0)
    elif N == 1:
        return (0 , 1)
    else:
        tu_arr : Tuple[int] = [None] * (N+1)

        tu_arr[0] = (1 , 0)
        tu_arr[1] = (0 , 1)
        
        for i in range(2 , N + 1):
            tu_arr[i] = (tu_arr[i - 1][0] + tu_arr[i - 2][0] , tu_arr[i - 1][1] + tu_arr[i - 2][1])

        return tu_arr[N]

num : int = int(input())

for i in range(num):
    usr_input : int = int(input())
    
    result = solution(usr_input)
    
    print(result[0] , result[1])