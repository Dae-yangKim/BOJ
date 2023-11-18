from typing import *
import sys

input = sys.stdin.readline

def dfs(node):
    for n in graph[node]:
        if check[n] == 0:
            check[n] = check[node]+1
            dfs(n)
            
for _ in range(int(input())):
    N = int(input())
    graph = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        v = int(input())
        graph[i].append(v)
    check = [0]*(N+1)
    dfs(1)
    print(check[N] if check[N] > 0 else 0)

print(graph)
print(check)