import sys
input = sys.stdin.readline

# 변수 생성
x , y , line , diagonal = map(int , input().split())

# 계산 

case_1 = (x + y) * line

if((x + y) % 2 == 0):
    case_2 = max(x , y) * diagonal
else:
    case_2 = ((max(x , y)-1) * diagonal) + line

case_3 = min(x , y) * diagonal + ((max(x , y) - min(x , y)) * line) 

print(min(min(case_1 , case_2) , case_3))