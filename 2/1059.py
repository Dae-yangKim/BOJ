from typing import *
import sys
input = sys.stdin.readline

def solution(S , n) -> int :

    if n in S:
        return 0

    S = sorted(S)

    if n < S[0]:
        target_list : List[int] = [i for i in range(1 , S[0])]
        value = len(target_list[:target_list.index(n)]) * len(target_list[target_list.index(n):]) + len(target_list[target_list.index(n)+1:])
        return value

    target_list : List[int] = []
    s : List[int] = S
    s.append(n) ; s = sorted(s)

    target_list.append(s[:s.index(n)]) ; target_list.append(s[s.index(n):])

    mini_value = target_list[0][-1]
    maximum_value = target_list[1][1]

    target_list = []
    for i in range(mini_value+1 , maximum_value):
        target_list.append(i)
    
    index = target_list.index(n)
    
    value = (len(target_list[:index]) * len(target_list[index:])) + len(target_list[index+1:])

    return value

L : int = int(input())
S : List[int] = list(map(int , input().split()))
n : int = int(input())

print(solution(S , n))