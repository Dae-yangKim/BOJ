import sys

input = sys.stdin.readline

n , d = map(int , input().split())
d = str(d)
arr = [i for i in range(1 , n + 1)]

count : int = 0

for num in arr:
    
    if d in str(num):
        count += str(num).count(d)

print(count)