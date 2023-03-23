import sys

input = sys.stdin.readline

N , K = map(int , input().split())
arr = list(map(int , input().split()))
result = []

for i in range(N - K + 1):
    summ = sum(arr[i : i+K])
    result.append(summ)

print(max(result))