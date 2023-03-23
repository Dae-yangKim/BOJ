from typing import *
import sys

input = sys.stdin.readline

T : int = int(input())
for _ in range(T):
    sentence = []
    N : int = int(input())
    
    arr = list(input().rstrip().split())
    
    sentence.append(arr.pop(0))
    for com in arr:
        if ord(com) - 64 <= ord(sentence[0]) - 64:
            sentence.insert(0 , com)
        else:
            sentence.append(com)
    
    print(''.join(sentence))