from typing import *
import sys

input = sys.stdin.readline

log_data : dict = {}

n : int = int(input())

for _ in range(n):
    
    name , state = map(str , input().split())
    
    log_data[name] = state

log_data = sorted(log_data.items() , key = lambda x : x[0] , reverse=True)

for data in log_data:

    if data[1] == 'enter':
        print(data[0])