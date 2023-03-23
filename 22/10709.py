from typing import *
import sys

input = sys.stdin.readline

def solution(city : str):

    distance : int = -1
    arr = []

    for comp in city:
        
        if comp == 'c':
            arr.append('0')
            distance = 0
        elif distance != -1:
            distance += 1
            arr.append(str(distance))
        else:
            arr.append(str(distance))
    
    return ' '.join(arr)

H , W = map(int , input().split())

for _ in range(H):
    
    city = input().rstrip()
    print(solution(city))