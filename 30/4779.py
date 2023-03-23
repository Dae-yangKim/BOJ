from typing import *
import sys

input = sys.stdin.readline

def d_a_q(s : str):
    
    if len(s) == 1:
        return "-"

    length = len(s) // 3
    left_block = d_a_q(s[:length])
    right_block = d_a_q(s[length * 2 :])
    
    join_ = (" " * len(left_block)).join([left_block , right_block])
    
    return join_

while True:
    try:   
        N : int = int(input())
        print(d_a_q("-" * (3 ** N)))
    except:
        break