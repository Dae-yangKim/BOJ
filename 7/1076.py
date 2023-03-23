from typing import *
import sys

input = sys.stdin.readline

table : dict = {
    "black" : ["0" , 1] ,
    "brown" : ["1" , 10] ,
    "red" : ["2" , 100] , 
    "orange" : ["3" , 1000] , 
    "yellow" : ["4" , 10000] , 
    "green" : ["5" , 100000] ,
    "blue" : ["6" , 1000000] ,
    "violet" : ["7" , 10000000] ,
    "grey" : ["8" , 100000000] ,
    "white" : ["9" , 1000000000]
}

color : List[str] = []
for i in range(3):
    data : str = input().strip() ; color.append(data)

result : int = int((table[color[0]][0] + table[color[1]][0])) * table[color[2]][1]
print(result)