from typing import *
import sys

input = sys.stdin.readline

#def make_tree(x, y):
#    root = {'data': (1, 1), 'left': None, 'right': None}
#    queue = [root]
#    while queue:
#        node = queue.pop(0)
#        if node['data'] == (x, y):
#            return root
#        if node['left'] is None:
#            node['left'] = {'data': (node['data'][0] + node['data'][1], node['data'][1]), 'left': None, 'right': None}
#            queue.append(node['left'])
#        if node['right'] is None:
#            node['right'] = {'data': (node['data'][0], node['data'][0] + node['data'][1]), 'left': None, 'right': None}
#            queue.append(node['right'])
#
#def find_node(node, x, y):
#    stack = [(node, 0, 0)]
#    while stack:
#        curr, left, right = stack.pop()
#        if curr['data'] == (x, y):
#            print(left, right)
#            return
#        if curr['left'] is not None:
#            stack.append((curr['left'], left+1, right))
#        if curr['right'] is not None:
#            stack.append((curr['right'], left, right+1))

x , y = map(int , input().split())

left = 0
right = 0

while x > 1 and y > 1:
    
    if x > y:
        left += x // y
        x %= y
    
    else:
        right += y // x
        y %= x

left += x - 1
right += y - 1

print(left , right)