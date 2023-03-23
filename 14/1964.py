import sys

input = sys.stdin.readline

N : int = int(input())
num = 5
change = 7
value = 3

for i in range(N - 1):
    num += change
    change += value

print(num % 45678)