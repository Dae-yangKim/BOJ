from typing import *
import sys

input = sys.stdin.readline

def selection_sort(arr : List[int] , K : int) -> None:
    global result

    count : int = 0

    for i in range(len(arr) - 1 , 0 , -1):
        
        max_num : int = max(arr[: i + 1])
        idx : int = arr.index(max_num)

        if i != idx:
            arr[i] , arr[idx] = arr[idx] , arr[i]
            count += 1

            if count == K:
                
                result.append(arr[idx])
                result.append(arr[i])
    
    if count < K:

        result = -1
        
A , K = map(int , input().split())
arr : List[int] = list(map(int , input().split()))
result = []
selection_sort(arr,  K)

if result != -1:
    print(result[0] , result[1])
else:
    print(-1)