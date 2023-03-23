from typing import *
import sys

input = sys.stdin.readline

point = [list(map(int , input().split())) for _ in range(3)]

len_ab = (abs(point[0][0] - point[1][0])**2 + abs(point[0][1] - point[1][1])**2)
len_bc = (abs(point[1][0] - point[2][0])**2 + abs(point[1][1] - point[2][1])**2)
len_ac = (abs(point[0][0] - point[2][0])**2 + abs(point[0][1] - point[2][1])**2)

length = [len_ab , len_bc , len_ac]
length_r = [len_ab**0.5 , len_bc**0.5 , len_ac**0.5]

length.sort()
length_r.sort()

d = (length[0] + length[1])

result = []

if length_r[2] >= length_r[0] + length_r[1]:
    result.append('X')
else:
    if length_r[0] == length_r[1] and length_r[1] == length_r[2]:
        result.append('Jung')
    elif length_r[0] == length_r[1] or length_r[1] == length_r[2] or length_r[2] == length_r[0]:
        if d < length[2]:
            result.append('Dunkak')
        elif d == length[2]:
            result.append('Jikkak')
        else:
            result.append('Yeahkak')
        result.append('2')
    else:
        if d < length[2]:
            result.append('Dunkak')
        elif d == length[2]:
            result.append('Jikkak')
        else:
            result.append('Yeahkak')
    
    result.append('Triangle')

print(''.join(result))