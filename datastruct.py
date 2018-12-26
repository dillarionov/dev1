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


class PriorityMinQueue():
    def __init__(self):
        self._queue = []

    def enqueue(self, priority, data):
        self._queue.append((priority, data))

    # def dequeue(self):
    #     min_index, min_p = 0, self._queue[0][0]
    #
    #     for i, el in enumerate(self._queue):
    #         if el[0] <= min_p:
    #             min_index, min_p = i, self._queue[i][0]
    #
    #     return self._queue.pop(min_index)

    def dequeue(self):
        if len(self._queue) == 0:
            return None

        (min_p, i) = min((el[0], i) for i, el in enumerate(self._queue))
        return self._queue.pop(i)