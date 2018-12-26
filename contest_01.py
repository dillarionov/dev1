import sys

n = int(sys.stdin.readline().rstrip())

longest, current = 0, 0
while n > 0:
    i = sys.stdin.readline().rstrip()
    if i == '0':
        longest = max(current, longest)
        current = 0
    else:
        current = current + 1

    n = n - 1

print max(current, longest)
