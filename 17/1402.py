from typing import *
import sys

input = sys.stdin.readline

def solution(a , b) -> str:
    
    for i in range(1 , int(a ** 0.5) + 1):

        for j in range(1 , int(a ** 0.5) + 1):

            num : int = i * j

            if num > a:
                break
            
            if num == a:
                
                if i + j == b:
                    return 'yes'
                else:
                    break

    return 'no'

T : int = int(input())
for _ in range(T):
    a , b = map(int , input().split())
    print(solution(a , b))
