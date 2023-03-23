from typing import *
import sys

input = sys.stdin.readline

def solution(sentence_1 : str , sentence_2 : str) -> bool:
    
    if sorted(sentence_1) == sorted(sentence_2):

        return True

    else:
        
        return False

N : int = int(input())

for _ in range(N):
    
    sentence_1 , sentence_2 = map(str , input().split())

    check : bool = solution(sentence_1 , sentence_2)

    if check:

        print(f"{sentence_1} & {sentence_2} are anagrams.")
    
    else:

        print(f"{sentence_1} & {sentence_2} are NOT anagrams.")