from typing import *
import sys

input = sys.stdin.readline

sentence = input()

sentence_0 = sentence.strip().split('1')
sentence_1 = sentence.strip().split('0')
arr = []
count = 0

if len(sentence_0) == 1:
    arr.append(count)
else:
    for element in sentence_0:
        
        if '0' in element:
            count += 1
    arr.append(count)

count = 0
if len(sentence_1) == 1:
    arr.append(count)
else:
    for element in sentence_1:

        if '1' in element:
            count += 1
    arr.append(count)

print(min(arr))