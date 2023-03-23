import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solution(n , i):
    global dp , count
    if (i not in dp.keys()) and (i == 0 or i == 9): dp[i] = 1
    elif i not in dp.keys() : dp[i] = 2

    if n == 2: return dp[i]
    
    if n == 1 : return 1
    elif i == 0 or i == 9: count = solution(n-1 , abs(i-1)) ; return count
    else : count = solution(n - 1 , i - 1) + solution(n - 1 , i + 1) ; return count

n = int(input())
dp = dict()
count = 0
for i in range(1 , 10):
    count += solution(n , i)
print(count)