from typing import *
import sys
input = sys.stdin.readline

def solution(N , kim , im) -> int:
    global arr
    tournament_count = 1

    kim_num = kim
    im_num = im

    while N != 1:
        
        tournament_arr = []

        if N % 2 == 0:
            for i in range(1 , N+1 , 2):
                tournament_arr.append([i , i+1])

            # 같은 라운드에 존재하는지 비교
            for i in tournament_arr:
                if (kim_num in i) and (im_num in i):
                    return tournament_count
                else: continue
            
            kim_num = (kim_num+1) // 2
            im_num = (im_num+1) // 2
            
            tournament_count += 1

            N //= 2

            continue

        else:
            for i in range(1 , N , 2):
                tournament_arr.append([i , i+1])
            tournament_arr.append(arr[-1])

            # 같은 라운드에 존재하는지 비교
            for i in tournament_arr:
                if type(i) != list:
                    continue
                if (kim_num in i) and (im_num in i):
                    return tournament_count
                else: continue

            kim_num = (kim_num+1) // 2
            im_num = (im_num+1) // 2
            arr[-1] = (arr[-1]+1) // 2

            tournament_count += 1

            N //= 2 ; N += 1

            continue
    
    return -1
    

N , kim , im = map(int , input().split())

arr : List[int] = [i for i in range(1 , N+1)]

print(solution(N , kim , im))