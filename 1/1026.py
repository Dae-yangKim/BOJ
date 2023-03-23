import sys
input = sys.stdin.readline

num = int(input())

arrA = sorted(list(map(int , input().split())))
arrB = list(map(int , input().split()))

sum = 0

for i in arrA:
    sum += i * max(arrB)
    max_index = arrB.index(max(arrB))
    arrB.pop(max_index)

print(sum)