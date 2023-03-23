from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())
for _ in range(N):
    sentence = list(map(int , input().rstrip()))
    length = len(sentence)
    idx = 0

    for i in range(length - 1 , 0 , -1):
        if sentence[i] > sentence[i - 1]:
            if i == length - 1:
                idx = length - 2
            else:
                idx = i - 1
            break
    
    sentence_a = sentence[:idx]
    sentence_b = sentence[idx:]

    if not sentence_a or not sentence_b:
        print('BIGGEST')
    else:
        sentence_b.sort()
        for i in range(len(sentence_b)):
            if sentence_b[i] > sentence[idx]:
                sentence_a.append(sentence_b.pop(i))
                sentence_a.extend(sentence_b)
                break
        
        print(''.join(map(str , sentence_a)))