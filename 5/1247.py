import sys

input = sys.stdin.readline

for i in range(3):
    num = int(input())
    sum_num = 0
    for j in range(num):
        usr_input = int(input())
        sum_num += usr_input

    if sum_num > 0 :
        print("+")
    elif sum_num < 0:
        print("-")
    else:
        print(0)