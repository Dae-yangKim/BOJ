from typing import *
import sys

input = sys.stdin.readline

min_num : int = 0
max_num : int = 11

while True:

    num : int = int(input())

    if num == 0:
        break

    answer : str = input().rstrip()

    if answer == 'too high' and num < max_num:
        max_num = num
    elif answer == 'too low' and num > min_num:
        min_num = num
    elif answer == 'right on':
        if num >= max_num or num <= min_num:
            print('Stan is dishonest')
        else:
            print('Stan may be honest')

        min_num = 0
        max_num = 11