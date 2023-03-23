from itertools import combinations
import sys

input = sys.stdin.readline

pd = [0 , 1 , 1]
n  = int(input())
for _ in range(n):

    target = int(input())
    idx = len(pd) - 1

    while True:
        num = pd[idx] + pd[idx - 1]

        if num >= target:
            break

        pd.append(num)
        idx += 1

    result_arr = ''
    length = 1
    condition = True

    while condition:

        for subset in combinations(pd , length):
            if sum(subset) == target:
                result_arr = subset
                condition = False
                break
        
        length += 1

    for sub in result_arr:
        print(sub , end = ' ')