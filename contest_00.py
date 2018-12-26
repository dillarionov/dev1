import sys

J = sys.stdin.readline().rstrip()
S = sys.stdin.readline().rstrip()

num = 0
for s in S:
    if s in J:
        num = num + 1

print num
