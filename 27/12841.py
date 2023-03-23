from typing import *
import sys

input = sys.stdin.readline

N : int = int(input())

center = map(int , input().split())
center_sum = [0]
summ = 0
for num in center:
    summ += num
    center_sum.append(summ)

left = map(int , input().split())
left_sum = [0]
summ = 0
for num in left:
    summ += num
    left_sum.append(summ)

right = map(int , input().split())
right_sum = [0]
summ = 0
for num in right:
    summ += num
    right_sum.append(summ)

cross : int = 1
data = {}

# prefix_sum
for idx in range(N):
    result = (center_sum[idx + 1] - center_sum[idx]) + (right_sum[N - 1] - right_sum[idx]) + (left_sum[idx] - left_sum[0])
    data[cross] = result
    cross += 1

data = sorted(data.items() , key = lambda x : (x[1] , x[0]))
print(data[0][0] , data[0][1])