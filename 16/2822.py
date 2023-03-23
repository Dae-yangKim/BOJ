from typing import *
import sys

input = sys.stdin.readline

score = []
for _ in range(8):
    score.append(int(input()))

max_score = sorted(score , reverse = True)
index = []

for idx in range(5):
    index.append(str(score.index(max_score[idx]) + 1))

print(sum(max_score[0:5]))
print(" ".join(sorted(index)))