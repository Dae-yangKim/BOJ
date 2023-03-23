from typing import *
import sys

input = sys.stdin.readline

def solution(nums : List[int] , order : List[int]) -> List[int]:
    for i in range(1 , len(order) + 1):
        if order[-i] == 0:
            continue
        else:
            nums : List[int] = change_list(nums , order[-i] , i)
            continue

    return nums

def change_list(nums : List[int] , order_element : int , i : int) -> List[int]:
    idx : int = nums.index(nums[-i]) + order_element
    number : int = nums.pop(-i)
    nums.insert(idx , number)

    return nums

num : int = int(input())
nums : List[int] = [i for i in range(1 , num+1)]
order : List[int] = list(map(int , input().split()))

result : List[int] = solution(nums , order)

for i in result:
    print(i , end = ' ')