from typing import *;
import sys

input = sys.stdin.readline

N , M = map(int , input().split())
package_arr : List[int] = []
normal_arr : List[int] = []

for i in range(M):
    package_price , normal_price = map(int , input().split())
    package_arr.append(package_price)
    normal_arr.append(normal_price)

num = N

if N % 6 == 0:
    num = N - 1
    
package_value = min(package_arr) * ((num // 6) + 1)
normal_value = min(normal_arr) * N
package_plus_normal_value = (min(package_arr) * (N//6)) + ((N - 6 * (N // 6)) * min(normal_arr))

print(min(package_value , min(normal_value , package_plus_normal_value)))