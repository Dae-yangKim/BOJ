import sys
from collections import deque
input = sys.stdin.readline

queue = deque()

buffer_size = int(input())

while True:
    usr_input = int(input())

    if usr_input == -1:
        if not queue: print("empty");break
        else:
            for i in queue:
                print(i , end = ' ')
            break

    if usr_input == 0:
        queue.popleft()
        continue

    if len(queue) == buffer_size:
        continue
    else:
        queue.append(usr_input)