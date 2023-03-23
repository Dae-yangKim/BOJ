import sys
input = sys.stdin.readline

top = []

N , K = map(int , input().split())

arr = [_ for _ in range(1 , N+1)]

def solution(arr , N , K):
    global top
    index = K - 1
    Max_Circle = len(arr)

    for i in range(N):
        if index >= Max_Circle:
            index = index % Max_Circle

        top.append(arr[index])
        arr.pop(index)

        index += (K - 1)
        Max_Circle = len(arr)

solution(arr , N , K)

print("<" , end = '')
for i in range(len(top)-1):
    print("{},".format(top[i]) , end = ' ')
print(top[-1] , end = '')
print(">")