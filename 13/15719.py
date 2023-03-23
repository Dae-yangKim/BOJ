import sys

input = sys.stdin.readline

N = int(input())
numbers = input().rstrip()
sum_number = sum(range(1 , N))
result = 0

for num in numbers:
    
    if num == ' ':
        
        continue
    
    else:

        result += int(num)

print(result - sum_number)