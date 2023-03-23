# 처음 풀이

from typing import *
import sys

input = sys.stdin.readline

#def binary_search(point : List[int] , start : int , end : int) -> int:
    
#    left : int = 0
#    right : int = len(point) - 1
    
#    while left < right:

#        mid = (left + right) // 2
        
#        if point[left] < start:
#            if not point[mid - 1] < start:
#                left = mid - 1
#            else:
#                left = mid
#        elif point[right] > end:
#            if not point[mid + 1] > end:
#                left = mid + 1
#            else:
#                right = mid
#        else:
#            return len(point[left : right + 1])
    
#    return 0

def binary_max(end : int) -> int:
    
    left = 0
    right = N - 1

    while left <= right:
        
        mid = (left + right) // 2

        if end < point[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return right

def binary_min(start : int) -> int:

    left = 0
    right = N - 1

    while left <= right:
        
        mid = (left + right) // 2

        if point[mid] < start:
            left = mid + 1
        else:
            right = mid - 1
    
    return right + 1


N , M = map(int , input().split())
point = sorted(list(map(int , input().split())))

for _ in range(M):
    start , end = map(int , input().split())
    print(binary_max(end) - binary_min(start) + 1)