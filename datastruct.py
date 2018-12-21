class Stack():
    def __init__(self):
        self._stack = []

    def push(self, el):
        self._stack.append(el)

    def pop(self):
        return self._stack.pop()

    def is_empty(self):
        return len(self._stack) == 0
