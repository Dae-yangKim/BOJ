n = int(input())
name_arr = []

for i in range(n):
    name = input()
    name_arr.append(name)

for i in name_arr:
    print(i.lower())