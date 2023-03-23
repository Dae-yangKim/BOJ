from typing import *
import sys

input = sys.stdin.readline

# 분할정복을 이용한 거듭제곱

def solution(a : int , b : int , c : int) -> int:
    if b == 0:
        return 1
    
    x = solution(a , b // 2 , c)
    
    if b % 2 == 0:
        return (x * x)%c
    else:
        return (x * x * a)%c # 수가 커지면 곱셈 시간이 늘어나니까 %c로 해서 처음부터 나머지만

A , B , C = map(int , input().split())
print(solution(A , B , C))