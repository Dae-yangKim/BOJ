from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
cycle_words = list()
for _ in range(N):
    flag = False
    word = deque(input().rstrip())
    for words in cycle_words:
        if ''.join(list(word)) in words:
            flag = True
            break
    if flag:
        continue
    words = list()
    for _ in range(len(word)):
        word.rotate(1)
        words.append(''.join(list(word)))
    cycle_words.append(words)
print(len(cycle_words))