from typing import *
import sys

input = sys.stdin.readline

data = dict()

while True:

    usrInput = input().rstrip()

    if usrInput == '*':
        break

    length : int = len(usrInput) - 1

    if length == 0:
        print(f"{usrInput} is surprising.")
    else:
        condition = []
        for i in range(length):
            for j in range(length - i):
                if usrInput[j] + usrInput[j + i + 1] not in data:
                    data[usrInput[j] + usrInput[j + i + 1]] = 1
                else:
                    data[usrInput[j] + usrInput[j + i + 1]] += 1
        
            if all(value == 1 for value in data.values()):
                condition.append(True)
            else:
                condition.append(False)

            data = dict()
        
        if False not in condition:
            print(f"{usrInput} is surprising.")
        else:
            print(f"{usrInput} is NOT surprising.")