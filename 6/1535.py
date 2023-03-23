from typing import *
import sys

input = sys.stdin.readline

def solution(health_point : List[int] , happy_point : List[int]) -> None:
    global result

    sejun : int = 100
    happy : int = 0

    backtracking_algorithm(health_point , happy_point , sejun , happy , 0)

# 백트래킹 알고리즘 응용
def backtracking_algorithm(health_point : List[int] , happy_point : List[int]\
    , sejun : int , happy : int , level :int) -> None:
    global result

    if sejun <= 0:
        return # backtracking

    for i in range(level , len(health_point)):
        happy += happy_point[i]
        sejun -= health_point[i]

        if sejun <= 0:
            happy -= happy_point[i]
            sejun += health_point[i]
            continue 

        backtracking_algorithm(health_point , happy_point , sejun , happy , i + 1)
        result.append(happy)
        happy -= happy_point[i] # 해 복구
        sejun += health_point[i] # hp 복구
        
N : int = int(input())

health_point : List[int] = list(map(int , input().split()))
happy_point : List[int] = list(map(int , input().split()))

result : List[int] = []

solution(health_point , happy_point)

if result:
    print(max(result))
else:
    print(0)    