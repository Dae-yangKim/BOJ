from typing import *
from collections import deque
import sys

input = sys.stdin.readline

def bfs(start , end , l):
    queue = deque()
    queue.append((start , 0))
    directions = [(1 , 2) , (2 , 1) , (1 , -2) , (2 , -1) , (-1 , 2) , (-2 , 1) , (-1 , -2) , (-2 , -1)]
    graph = [[0 for _ in range(l)] for _ in range(l)]
    graph[start[0]][start[1]] = 1

    while queue:
        current , distance = queue.popleft()
        x , y = current

        if current == end:
            return distance
        
        for dx , dy in directions:
            nx , ny = x + dx , y + dy
            next_coord = (nx , ny)

            if next_coord[0] < 0 or next_coord[1] < 0:
                continue

            if next_coord[0] > (l - 1) or next_coord[1] > (l - 1):
                continue

            if graph[next_coord[0]][next_coord[1]] != 1:
                queue.append((next_coord , distance + 1))
                graph[next_coord[0]][next_coord[1]] = 1

    return -1

N : int = int(input())
for i in range(N):
    l : int = int(input())
    start = tuple(map(int , input().split()))
    end = tuple(map(int , input().split()))
    print(bfs(start , end , l))