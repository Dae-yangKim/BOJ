from typing import *
import sys

input = sys.stdin.readline

def solution(arr : List[int]) -> int:
    global max_number

    max_number = arr.pop(arr.index(max(arr)))

    arr = check_condtion(arr)

    if arr == -1:
        return -1
    else:
        second_max_number= arr.pop(arr.index(max(arr)))
        third_max_number = arr.pop(arr.index(max(arr)))
        
        return max_number + second_max_number + third_max_number

def check_condtion(arr : List[int]):
    global max_number
    
    while len(arr) >= 3:
            
        count : int = 0

        for i in range(len(arr) - 1):
            if arr[i] + arr[i+1] <= max_number:
                count += 1
            else:
                continue 
                    
        if count == len(arr) - 1:
            max_number = arr.pop(arr.index(max(arr)))
            continue
        else:
            return arr

    if sum(arr) > max_number:
        return arr
    else:
        return -1

num : int = int(input())
arr : List[int] = []

for i in range(num):
    usr_input : int = int(input())
    arr.append(usr_input)

max_number : int = 0

result : int = solution(arr)
print(result)