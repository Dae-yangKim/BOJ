from typing import *
import sys

input = sys.stdin.readline

number_set : set = set()
N : int = int(input())

for i in range(N):
    command : List[str] = list(map(str , input().split()))

    if command[0] == "add":
        number_set.add(command[1])
    elif command[0] == "remove":
        number_set.remove(command[1])
    elif command[0] == "check":
        if command[1] in number_set:
            print(1)
        else: print(0)
    elif command[0] == "toggle":
        if command[1] in number_set:
            number_set.remove(command[1])
        else:
            number_set.add(command[1])
    elif command[0] == "all":
        number_set = {str(i) for i in range(1 , 21)}
    else:
        number_set = set()