import sys
input = sys.stdin.readline

number_arr = map(int , input().split())

sentence = ""
for i in number_arr:
    sentence += str(i)

if sentence == "12345678":
    print("ascending")
elif sentence == "87654321":
    print("descending")
else:
    print("mixed")