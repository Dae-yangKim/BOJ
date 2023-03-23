from typing import *
import sys

input = sys.stdin.readline

def eratos(n : int , k : int):
    
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    count : int = 0

    for i in range(2 , n + 1):
        for j in range(i , n + 1 , i):
            if primes[j]:
                primes[j] = False
                count += 1

                if count == k:
                    return j

n , k = map(int , input().split())
print(eratos(n , k))