import sys

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):

    name , day , month , year = input().rstrip().split()
    day , month , year = map(int , (day , month , year))
    arr.append((year , month , day , name))

arr.sort()
print(arr[-1][3])
print(arr[0][3])