from typing import *
from collections import deque
import sys

input = sys.stdin.readline


def BFS(arr , x , y) -> int:
    
    dx = [-1 , 1 , 0 , 0]
    dy = [0 , 0 , -1 , 1]

    queue = deque()
    queue.append((x , y))

    while queue:
        
        x , y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                queue.append((nx , ny))
                arr[nx][ny] = arr[x][y] + 1
    
    return arr[N - 1][M - 1]

N , M = map(int , input().split())
arr : List[int] = []

for _ in range(N):
    arr.append(list(map(int , input().rstrip())))

print(BFS(arr , 0 , 0))