from typing import *
import sys

input = sys.stdin.readline

# 분할정복 거듭제곱
def d_a_c(a , b):

    if (a , b) in data:
        return data[(a , b)]
    
    if b == 0:
        result = 1
    else:
        x = d_a_c(a , b//2)
        if b % 2 == 0:
            result = (x * x)
        else:
            result = (x * x * a)
    
    data[(a , b)] = result
    return result

p : int = int(input())
n : int = int(input())
data = {}

count = 0
for i in range(p):
    x = d_a_c(i , n)
    for j in range(p):
        y = d_a_c(j , n)
        for k in range(p):
            z = d_a_c(k , n)
            if (x + y - z) % p == 0:
                count += 1
print(count)