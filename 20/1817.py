from typing import *
import sys

input = sys.stdin.readline

N , M = map(int , input().split())
try:
    temp : int = M

    arr : List[int] = list(map(int , input().split()))

    count : int = 0
    for i in arr:

        if temp <= i:
            temp = M
            count += 1
            temp -= i
        else:
            temp -= i

    print(count + 1)
except:
    print(0)