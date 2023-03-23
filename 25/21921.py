from typing import *
import sys

input = sys.stdin.readline

N , X = map(int , input().split())
arr = list(map(int , input().split()))
prefix_sum = [0] * (N + 1)

for i in range(1 , N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

blog_arr = []
for i in range(X , N + 1):
    blog_arr.append(prefix_sum[i] - prefix_sum[i - X])

if len(set(blog_arr)) == 1 and blog_arr[0] == 0:
    print('SAD')
else:
    maxx = max(blog_arr)
    print(maxx)
    print(blog_arr.count(maxx))