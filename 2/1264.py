import sys
input = sys.stdin.readline

arr = ['a','e','i','o','u']

while True:
    count = 0
    usr_input = input()

    if usr_input == '#':
        break

    for i in usr_input:
        if i.lower() in arr:
            count += 1
    
    print(count)