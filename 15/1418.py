import sys
input = sys.stdin.readline

def solution(n):
    factor = 2
    factors = []
    
    while(factor**2 <= n):
        while(n % factor == 0):
            factors.append(factor)
            n = n // factor
        factor += 1
    
    if n > 1:
        factors.append(n)
    
    return factors

N = int(input())
K = int(input())
count = 0

for n in range(1 , N + 1):
    
    factors = solution(n)
    
    if not factors:
        continue

    if max(factors) <= K:
        count +=1

print(count+1)    