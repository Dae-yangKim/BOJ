def solution(n):
    result = 0
    for i in range(1 , n + 1):
        result += i * sum(j for j in range(1 , i + 2))
    
    return result

num = int(input())
for i in range(num):
    n = int(input())
    print(solution(n))