class Stack():
    def __init__(self):
        self._stack = []

    def push(self, el):
        self._stack.append(el)

    def pop(self):
        return self._stack.pop()

    def is_empty(self):
        return len(self._stack) == 0


class NextNode():
    def __init__(self, val=None, _next=None):
        self.val = val
        self._next = _next

    def __repr__(self):
        return str(self.val)


class ChildrenNode():
    def __init__(self, val=None, children=None):
        self.val = val or -1
        self.children = children or []

    def __repr__(self):
        return str(self.val)
