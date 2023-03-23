from typing import *
import sys

input = sys.stdin.readline

def solution(point) -> int:
    
    vec_a : int = point[0][0] * point[1][1] + point[1][0] * point[2][1] + point[2][0] * point[0][1]
    vec_b : int = point[1][0] * point[0][1] + point[2][0] * point[1][1] + point[0][0] * point[2][1]

    return vec_a - vec_b

point = []
for _ in range(3):
    point.append(tuple(map(int , input().split())))

outer_product : int = solution(point)

if outer_product < 0:
    print(-1)
elif outer_product > 0:
    print(1)
else:
    print(0)