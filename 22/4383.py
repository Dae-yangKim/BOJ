from typing import *
import sys

input = sys.stdin.readline

def solution(n , arr) -> str:

    check_arr = [i for i in range(1 , n)]
    result_arr = []

    for i in range(len(arr) - 1):
        
        result : int = abs(arr[i] - arr[i + 1])

        if result not in result_arr:
            result_arr.append(result)
    
    if sorted(result_arr) == check_arr:
        return 'Jolly'
    else:
        return 'Not jolly'
    

while True:

    try:
        arr = list(map(int , input().split()))
        print(solution(arr[0] , arr[1:]))
    except:
        break