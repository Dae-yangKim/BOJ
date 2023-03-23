from typing import *
import sys
input = sys.stdin.readline

h , m , s = map(int , input().split())
usr_input = int(input())

m += usr_input // 60
s += usr_input % 60

while s >= 60:
    m_to_s = s // 60
    s = s %60
    m += m_to_s

while m >= 60:
    h_to_m = m // 60
    m = m % 60
    h += h_to_m

while h >= 24:
    h = h - 24

print(h , m , s)