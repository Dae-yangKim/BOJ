from typing import *
import sys

input = sys.stdin.readline

def find_prime(N : int):
    
    if N <= 2:
        return [N , ]
    
    for idx in range(2 , N):
        
        if N % idx == 0:
            arr = []
            val_a = find_prime(idx)
            val_b = find_prime(int(N / idx))

            arr = val_a + val_b
            return arr
    
    return [N , ]

T : int = int(input())

for _ in range(T):

    N : int = int(input())

    arr = sorted(find_prime(N))
    set_arr = set(arr)
        
    for num in set_arr:

        print(f"{num} {arr.count(num)}")