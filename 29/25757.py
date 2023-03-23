from typing import *
import sys

input = sys.stdin.readline

game = {
    "Y" : 1 ,
    "F" : 2 ,
    "O" : 3
}

N , G = map(str , input().rstrip().split())
bound : int = game[G]
players = []
for _ in range(int(N)):
    players.append(input().rstrip())

players = set(players)

print(len(players) // bound)