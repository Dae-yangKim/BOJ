from typing import *
import sys

input = sys.stdin.readline

while True:
    n , k = map(int , input().split())
    if n == 0 and k == 0:
        break
    # 변수 선언 (나중에 나눠야 하기에)
    a : int = 1 ; b : int = 1
    n_k : int = n - k
    
    for i in range(n , max(k , n_k) , -1):
        a *= i
    for i in range(1 , min(k , n_k) + 1):
        b *= i
    
    print(a // b)