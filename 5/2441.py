num = int(input())

for i in range(num , 0 , -1):
    print("{}{}".format(" " * (num - i) , "*" * i))