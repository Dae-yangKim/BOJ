from typing import *
import sys

input = sys.stdin.readline

def solution(num_list) -> List[int]:
    result = []
    while True:
        pop_num : int = num_list.pop(0)
        result.append(pop_num)

        if not num_list:
            break
        else:     
            insert_num = num_list.pop(0)
            num_list.append(insert_num)

    return result

N : int = int(input())
num_list = [i for i in range(1 , N + 1)]

arr = solution(num_list)
for i in arr:
    print(i , end = ' ')