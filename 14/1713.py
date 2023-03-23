import sys

input = sys.stdin.readline

N = int(input())
arr = [0] * N

for i in range(N):
    
    arr[i] = int(input())

calc_add = arr[1] - arr[0]
calc_mul = arr[1] // arr[0]

if calc_add + arr[1] == arr[2]:
    print(arr[-1] + calc_add)
else:
    print(arr[-1] * calc_mul)