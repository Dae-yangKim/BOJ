from typing import *
import sys

input = sys.stdin.readline

def solution(name_element : List[str]) -> str:

    element_set = set(name_element)
    element_quantity_dict = dict()
    odd_count : int = 0
    # 회문 가능한 형태
    
    for i in element_set:
        if name_element.count(i) % 2 != 0:
            odd_count += 1
            element_quantity_dict[i] = name_element.count(i)
        else: element_quantity_dict[i] = name_element.count(i)

    # 처리

    result_name : List[str] = []

    if odd_count > 1:
        return "I'm Sorry Hansoo"
    else:
        # 시작 처리 (홀수개 존재하는 경우)
        for i in list(element_quantity_dict.keys()):
            if element_quantity_dict[i] % 2 != 0:
                result_name.append(i)
                element_quantity_dict[i] -= 1
            else : continue
        
        # 처리
        element_set = sorted(list(element_set) , reverse=True) # 반대로 정렬
        for i in element_set:
            for j in range(element_quantity_dict[i]//2):
                result_name.insert(0 , i)
                result_name.append(i)
            
        return ''.join(s for s in result_name)
        
name : str= input().strip()

name_element : List[str] = []

for i in name:
    name_element.append(i)

result : str = solution(sorted(name_element , reverse=True))

print(result)