N = int(input())
sentence = input()

A = sentence.count('A')
B = sentence.count('B')

if A > B:
    print('A')
elif A < B:
    print('B')
else:
    print('Tie')