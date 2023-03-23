from typing import *
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def make_graph_dict() -> None:
    global graph , graph_dict

    for i in graph:
        graph_dict[i[0]].append(i[1])
        graph_dict[i[1]].append(i[0])

def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def find_connected_components(graph):
    visited = set()
    connected_components = []
    for node in graph:
        if node not in visited:
            connected_component = set()
            dfs(graph, node, connected_component)
            connected_components.append(connected_component)
            visited |= connected_component
    return connected_components

graph_dict : dict = {}
N , M = map(int , input().split())
graph : List[List[str]] = [list(map(str , input().split())) for _ in range(M)]
for i in range(N):
    graph_dict[str(i + 1)] = []
make_graph_dict()
result = find_connected_components(graph_dict)
print(len(result))