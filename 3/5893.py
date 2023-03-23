num = input()
length = len(num) - 1
value = 0

def solution(value):
    arr = []
    while value > 0:
        num = value % 2
        arr.append(num)
        value = value // 2
    
    return arr

for i in num:
    if i == "1":
        value += 2**length
        length = length - 1
    else:
        length = length - 1

value = value * 17

arr = solution(value)
sentence = ""
for i in range(len(arr) - 1 , 0 , -1):
    sentence += str(arr[i])

print(sentence)