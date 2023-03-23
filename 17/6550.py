from typing import *
import sys

input = sys.stdin.readline

def solution(s : str , t : str) -> str:

    while True:

        result = []
        t = list(t)

        for sub in s:
            
            if sub in t:
                result.append(sub)
                del[t[:t.index(sub) + 1]]
        
        if ''.join(result) == s:
            return 'Yes'
        else:
            return 'No'

while True:
    try:
        s , t = map(str , input().rstrip().split())
        print(solution(s , t))
    except:
        break
