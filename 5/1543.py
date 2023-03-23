import sys

input = sys.stdin.readline

def sentence_check(sentence , check):
    global count
    
    end = len(check)
    
    while len(sentence) >= len(check):

        index = sentence.find(check)
        if index == -1:
            break
        count += 1
        sentence = sentence[index + end : ]    
    
    return count
count = 0
sentence = input().strip()
check = input().strip()

result = sentence_check(sentence , check)
print(result)