import sys
input = sys.stdin.readline

while True:
    num = int(input())

    if num == 0:
        break

    num = str(num)
    
    for i in range(len(num)):
        if num[i] == num[-(i+1)]:
            result = "yes"
        else:
            result = "no"
            break

    print(result)        