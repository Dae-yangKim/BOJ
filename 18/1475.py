from typing import *
import sys

input = sys.stdin.readline

def solution(num : str) -> int:
    
    number : str = '01234578'
    count : int = 0
    six_and_nine = num.count('6') + num.count('9')

    if six_and_nine % 2 == 0:
        count += six_and_nine // 2
    else:
        count += (six_and_nine // 2) + 1

    for i in number:
        
        value : int = num.count(i)

        if value > count:
            count = value
    
    return count

num : int = int(input())
print(solution(str(num)))