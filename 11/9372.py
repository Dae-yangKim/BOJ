from typing import *
import sys

input = sys.stdin.readline

T : int = int(input())
graph = []

for i in range(T):
    
    N , M = map(int , input().split())

    for i in range(M):

        graph.append([map(int , input().split())])
    
    print(N - 1)    