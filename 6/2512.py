from typing import *
import sys

input = sys.stdin.readline

def solution(num_arr : List[int] , condition : int) -> int:
    if sum(num_arr) <= condition:
        return max(num_arr)
    else:
        result : int = binary_search(num_arr , condition , 0 , max(num_arr))

    return result

def binary_search(num_arr : List[int] , condition : int ,  left : int , right : int) -> int:
    result : int = 0
    while left <= right :
        middle : int = (left + right) // 2
        
        sum_number : int = 0
    
        for i in num_arr:
            if i > middle :
                sum_number += middle
            else:
                sum_number += i
        
        if sum_number > condition:
            right = middle
            continue
        elif (sum_number <= condition) and (middle > result):
            result = middle
            left = middle
            continue
        else:
            return result

num : int = int(input())
num_arr : List[int] = list(map(int , input().split()))
condition : int = int(input())
print(solution(num_arr , condition))