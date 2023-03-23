hint = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

a = input()
b = input()
arr = []

# 알파벳의 아스키 코드에서 65를 빼면 hint에서 해당 알파벳의 인덱스를 구할 수 있다. 이를 arr 배열에 삽입한다.
for i in range(len(a)):
	arr.append(hint[ord(a[i]) - 65])
	arr.append(hint[ord(b[i]) - 65])

temp = []

# arr의 길이가 2가 될 때까지 반복
while len(arr) != 2:
	for idx in range(1, len(arr)):
    	# 인접한 값들의 합을 10으로 나누었을 때, 그 나머지는 1의 자리와 같다.
		temp.append((arr[idx] + arr[idx-1]) % 10)

	arr = temp
	temp = []

print(f"{arr[0]}{arr[-1]}")