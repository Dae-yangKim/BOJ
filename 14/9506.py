from typing import *
import sys

input = sys.stdin.readline

while True:
        
    arr = []

    n : int = int(input())

    if n == -1:
        break

    for i in range(1 , n):

        if n % i == 0:

            arr.append(i)

    if sum(arr) == n:

        print(str(n) + " " + "=" + " " , end = "")
            
        for i in range(len(arr)):

            if i == (len(arr) - 1):

                print(str(arr[i]))
                
            else:

                print(str(arr[i]) + " " + "+" + " " , end = "")

    else:
        print(f"{n} is NOT perfect.")