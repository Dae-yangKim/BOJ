import sys

input = sys.stdin.readline

N , M = map(int , input().split())
arr = sorted(list(map(int , input().split())))

print(arr[M - 1])