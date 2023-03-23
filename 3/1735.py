import sys

input = sys.stdin.readline

# 유클리드 알고리즘

def gcd(a , b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

a_child , a_mother = map(int , input().split())
b_child , b_mother = map(int , input().split())

# 유리수 계산 코드

child_result = 0
mother_result = 0

if a_mother == b_mother:
    child_result = a_child + b_child
    mother_result = a_mother
else:
    child_result = (a_child * b_mother) + (b_child * a_mother)
    mother_result  = a_mother * b_mother

# 기약함수로 만드는 코드

gcd_value = gcd(mother_result , child_result)

if gcd_value == 1:
    print(child_result , mother_result)
else:
    print(child_result // gcd_value , mother_result // gcd_value)