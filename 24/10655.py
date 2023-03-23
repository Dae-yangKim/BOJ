from typing import *
import sys
import math

input = sys.stdin.readline

N : int = int(input())
check_point = [list(map(int , input().split())) for _ in range(N)]

distance = [0]
for i in range(N - 1):
    dist = abs(check_point[i + 1][0] - check_point[i][0]) + abs(check_point[i + 1][1] - check_point[i][1])
    distance.append(dist)

totalDistance = sum(distance)
min_dist = math.inf

for i in range(1 , N - 1):
    dist = totalDistance - (distance[i + 1] + distance[i]) + abs(check_point[i - 1][0] - check_point[i + 1][0]) + abs(check_point[i - 1][1] - check_point[i + 1][1])
    min_dist = min(min_dist , dist)

print(min_dist)