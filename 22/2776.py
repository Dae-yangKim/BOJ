from typing import *
import sys

input = sys.stdin.readline

T : int = int(input())

for _ in range(T):
    
    n1 : int = int(input())
    note_1 = set(map(int , input().split()))
    n2 : int = int(input())
    note_2 = list(map(int , input().split()))

    for i in note_2:
        
        if i in note_1:
            print(1)
        else:
            print(0)