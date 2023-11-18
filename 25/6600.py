import sys; input = sys.stdin.readline
from math import pi

while True:
    try: # EOF 처리
        x1, y1, x2, y2, x3, y3 = map(float, input().split())
    except:
        break

    # 풀이에서 식 정리를 보자.
    # 필요한 제곱들
    x12 = x1 ** 2
    x22 = x2 ** 2
    x32 = x3 ** 2
    y12 = y1 ** 2
    y22 = y2 ** 2
    y32 = y3 ** 2

    # b, a, r을 순서대로 구하자
    b = ((x22 - x12 + y22 - y12) * (2 * x1 - 2 * x3) - (x32 - x12 + y32 - y12) * (2 * x1 - 2 * x2)) / ((2 * y1 - 2 * y2) * (2 * x1 - 2 * x3) - (2 * y1 - 2 * y3) * (2 * x1 - 2 * x2))
    try:
        a = (x22 - x12 + y22 - y12 - (2 * y1 - 2 * y2) * b) / (2 * x1 - 2 * x2)
    except:
        a = (x32 - x12 + y32 - y12 - (2 * y1 - 2 * y3) * b) / (2 * x1 - 2 * x3)
    r = ((x1 + a) ** 2 + (y1 + b) ** 2) ** 0.5

    # 원의 둘레는 2 * pi * r
    print(format(2 * pi * r, '.2f'))