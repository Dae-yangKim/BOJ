from typing import *
import sys

input = sys.stdin.readline

def solution(sentence_a : str , sentence_b : str) -> int:

    count : int = 0

    if sentence_a in sentence_b:
        return 0
    
    sentence_length_b_to_a : int = len(sentence_b) - len(sentence_a)

    if sentence_length_b_to_a == 0:

        for i in range(len(sentence_a)):
            if sentence_a[i] != sentence_b[i]: count += 1
            else : continue
    
    else:

        minimum_arr : List[int] = []
        plus_num : int = 0
        
        while plus_num <= sentence_length_b_to_a:
            
            minimum_num : int = 0

            for i in range(len(sentence_a)):
                if sentence_a[i] != sentence_b[i + plus_num] : minimum_num += 1
                else : continue

            minimum_arr.append(minimum_num)

            plus_num += 1             

        return min(minimum_arr)
    
    return count

sentence_a , sentence_b = input().split()

result = solution(sentence_a , sentence_b)

print(result)