from typing import *
import sys

input = sys.stdin.readline

def solution(N : int) -> int:
    global arr

    final_len : int = 0

    for i in range(N + 1):

        target_list = [N , i]
        j : int = 0

        while True:
            
            num : int = target_list[j] - target_list[j + 1]
            j += 1

            if num < 0:
                break
            
            target_list.append(num)
            if final_len < len(target_list):
                final_len = len(target_list)
                arr = target_list
        
    return final_len

N : int = int(input())
arr : List[int] = []

print(solution(N))
arr = [str(arr[i]) for i in range(len(arr))]
print(' '.join(arr))