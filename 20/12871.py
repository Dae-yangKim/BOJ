from typing import *
import sys

input = sys.stdin.readline

sentence_1 : str = input().rstrip()
sentence_2 : str = input().rstrip()

length_1 : int = len(sentence_1)
length_2 : int = len(sentence_2)

if sentence_1 * length_2 == sentence_2 * length_1:
    print(1)
else:
    print(0)