import sys
input = sys.stdin.readline

def gcd(a , b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

a , b = map(int , input().split())
result_a , result_b = b - a , b

condition = gcd(result_a , result_b)

if condition == 1:
    print(result_a , result_b)
else:
    print(result_a//condition , result_b//condition)