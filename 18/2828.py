from typing import *
import sys

input = sys.stdin.readline

def solution(N : int , M : int , J : int) -> int:
    global arr

    position : List[int] = [i for i in range(1 , M + 1)]
    count : int = 0
    idx : int = 0

    while idx + 1 <= len(arr):

        if arr[idx] in position:
            idx += 1
            continue
        else:
            
            if arr[idx - 1] < arr[idx]:

                for i in range(len(position)):
                    position[i] += 1
                
                count += 1
            
            else:
                
                for i in range(len(position)):
                    position[i] -= 1
                
                count += 1
    
    return count

N , M = map(int , input().split())
J = int(input())
arr = [0] * J
for idx in range(J):
    arr[idx] = int(input())

print(solution(N , M , J))