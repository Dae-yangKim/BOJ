from typing import *
import sys

input = sys.stdin.readline

pw_dict : dict = {}

N , M = map(int , input().split())

for i in range(N):
    address , pw = map(str , input().split())
    pw_dict[address] = pw

for i in range(M):
    address : str = input().strip()
    print(pw_dict[address])