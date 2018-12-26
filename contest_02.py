import sys

n = int(sys.stdin.readline().rstrip())

prev, curr = None, None
while n > 0:
    curr = sys.stdin.readline().rstrip()
    if curr != prev:
        print curr
        prev = curr

    n = n - 1
