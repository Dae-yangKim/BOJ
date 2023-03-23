arr = []
for i in range(5):
    usr_input = int(input())
    
    if usr_input < 40:
        usr_input = 40
    
    arr.append(usr_input)

value = sum(arr)
print(value//5)