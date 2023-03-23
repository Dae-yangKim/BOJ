from typing import *
import sys

input = sys.stdin.readline

def solution(angle : List[int]) -> str:
    angle_sum : int= sum(angle)
    if angle_sum != 180:
        return "Error"
    else:
        if len(set(angle)) == 1:
            return "Equilateral"
        elif len(set(angle)) == 2:
            return "Isosceles"
        elif len(set(angle)) == 3:
            return "Scalene"
angle : List[int] = []
for i in range(3):
    angle.append(int(input()))
print(solution(angle))