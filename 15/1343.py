from typing import *
import sys

input = sys.stdin.readline

sentence = input()

sentence = sentence.replace("XXXX" , "AAAA")
sentence = sentence.replace("XX" , "BB")

if 'X' in sentence:
    print(-1)
else:
    print(sentence)