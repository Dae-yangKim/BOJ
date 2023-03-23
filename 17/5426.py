import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    
    sentence = input().rstrip()
    length = len(sentence)
    num = 1
    
    while True:
        if num ** 2 == length:
            break
        num += 1
    
    result = ""
    
    for i in range(num , 0 , -1):
        result += sentence[i -1 :: num]

    print(result)