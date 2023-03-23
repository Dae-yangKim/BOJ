from typing import *
import sys

input = sys.stdin.readline

tree_data : dict = {}
N : int = int(input())

def preorder(root):
    global state
    state += root

    left = tree_data[root][0]
    right = tree_data[root][1]

    if left != '.':
        preorder(left)
    
    if right != '.':
        preorder(right)
    
    return state

def inorder(root):
    global state
    
    left = tree_data[root][0]

    if left != '.':
        inorder(left)
    
    state += root

    right = tree_data[root][1]

    if right != '.':
        inorder(right)
    
    return state

def postorder(root):
    global state

    left = tree_data[root][0]
    right = tree_data[root][1]

    if left != ".":
        postorder(left)
    
    if right != '.':
        postorder(right)
    
    state += root

    return state
for i in range(N):
    center , left , right = map(str , input().split())
    tree_data[center] = [left , right]

state = ""
state = preorder('A')
print(state)
state = ""
state = inorder('A')
print(state)
state = ""
state = postorder('A')
print(state)