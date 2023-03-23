from typing import *
import sys

input = sys.stdin.readline

data : dict = {}

N , M = map(int , input().split())
for i in range(N):
    guiter , information = map(str , input().split())
    data[guiter] = information