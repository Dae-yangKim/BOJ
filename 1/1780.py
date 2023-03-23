import sys
input = sys.stdin.readline

n = int(input())
map = [list(map(int , input().split())) for _ in range(n)]

result = []

def solution(x , y , n):
    mini_map = map[x][y]
    for i in range(x , x+n):
        for j in range(y , y+n):
            if mini_map != map[i][j]:
                solution(x , y , n//3)
                solution(x+n//3 , y , n//3)
                solution(x+((n*2)//3) , y , n//3)
                solution(x , y+n//3 , n//3)
                solution(x+n//3 , y+n//3 , n//3)
                solution(x+((n*2)//3) , y+n//3 , n//3)
                solution(x , y+((n*2)//3) , n//3)
                solution(x+n//3 , y+((n*2)//3) , n//3) 
                solution(x+((n*2)//3) , y+((n*2)//3) , n//3)
                return

    
    if mini_map == -1:
        result.append(-1)
    elif mini_map == 0:
        result.append(0)
    elif mini_map == 1:
        result.append(1)
    else:
        mini_map = set(mini_map)
        result.append(list(mini_map)[0])

solution(0 , 0 , n)
print(result.count(-1))
print(result.count(0))
print(result.count(1))