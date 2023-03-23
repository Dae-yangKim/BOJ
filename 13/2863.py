from typing import *

num : List[List[int]] = []

num.append(list(map(int , input().split())))
num.append(list(map(int , input().split())))

calc1 = (num[0][0] / num[1][0]) + (num[0][1] / num[1][1])
calc2 = (num[1][0] / num[1][1]) + (num[0][0] / num[0][1])
calc3 = (num[1][0] / num[0][0]) + (num[1][1] / num[0][1])
calc4 = (num[0][1] / num[0][0]) + (num[1][1] / num[1][0])

result = [calc1 , calc2 , calc3 , calc4]

print(result.index(max(result)))