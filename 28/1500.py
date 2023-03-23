from typing import *
import sys

input = sys.stdin.readline

S , K = map(int , input().split())

print((S // K) ** (K - S % K) * (S // K + 1) ** (S % K))