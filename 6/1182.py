from typing import *
import sys

input = sys.stdin.readline

N , S = map(int , input().split())
arr : List[int] = list(map(int , input().split()))
count : int = 0

def solution(index : int , sub_sum : int) -> None:
    global count

    if index >= N:
        return

    sub_sum += arr[index]

    if sub_sum == S:
        count += 1
    
    solution(index + 1 , sub_sum)

    solution(index + 1 , sub_sum - arr[index])

solution(0 , 0)
print(count)