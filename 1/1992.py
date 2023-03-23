import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
num_map = [input() for _ in range(n)]
result_arr = []

def solution(a , b , n):
    color = num_map[a][b : n-1]
    for i in range(a , a+n):
        for j in range(b , b+n):
            if color != num_map[i][j]:
                #solution(x , y , n//2)
                #solution(x+n//2 , y , n//2)
                #solution(x , y+n//2 , n//2)
                #solution(x+n//2 , y+n//2 , n//2)
                solution(a , b , n//2)
                solution(a , b+n//2 , n)
                solution(a+n//2 , b , n//2)
                solution(a+n//2 , b+n//2 , n)
                return 
    if a == 0 or a == n-1:
        result_arr.append("("+color)
    elif b == 0 or b == n-1:
        result_arr.append(color+")")
    else:
        result_arr.append(color)

solution(0 , 0 , n)
print(result_arr)
print(num_map)