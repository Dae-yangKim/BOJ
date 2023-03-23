from typing import *
import sys

input = sys.stdin.readline

sentence = input().rstrip().split('What is ')

for sub in sentence:

    if not sub[0].isupper():
        question_number = sub.find('?')
        print('Forty-two is' , sub[: question_number+1].replace('?' , '.'))