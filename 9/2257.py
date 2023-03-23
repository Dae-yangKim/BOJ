from typing import *
import sys

input = sys.stdin.readline

def solution(chemical_formula : str) -> None:
    global stack 

    chemical_formula = list(chemical_formula)

    for sentence in chemical_formula:
        
        if sentence == "(":
            stack.append(sentence)
        
        elif sentence == ")":
            check : int = 0
            
            while True:
                target : str = stack.pop()
                
                if target == "(":
                    break
                    
                check += target
            
            stack.append(check)
        
        elif sentence in data:
            stack.append(data[sentence])
        
        else:
            stack[-1] *= int(sentence)

data = {
    "H" : 1 ,
    "C" : 12 ,
    "O" : 16
}

stack = []
chemical_formula : str = input().strip()
solution(chemical_formula)
print(sum(stack))