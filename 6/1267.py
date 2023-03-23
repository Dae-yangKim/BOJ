from typing import *
import sys

input = sys.stdin.readline

def yongshick_function(arr : List[int]) -> int:
    result : int = 0
    for i in arr:
        result += ((i // 30) + 1) * 10
    return result

def minshick_function(arr : List[int]) -> int:
    result : int = 0
    for i in arr:
        result += ((i // 60) + 1) * 15
    return result

num : int = int(input())
arr : List[int] = list(map(int , input().split()))

y : str = "Y"
m : str = "M"

yongshick : int = yongshick_function(arr)
minshick : int = minshick_function(arr)

result = min(yongshick , minshick)
if result == yongshick and result == minshick:
    print(y , m , result)
elif result == yongshick:
    print(y , result)
else:
    print(m , result)