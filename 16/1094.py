a = int(input())
count = 0

while a != 0:

    if a % 2 == 1:
        count += 1
    
    a = a // 2

print(count)