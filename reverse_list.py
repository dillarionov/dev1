class Node():
    def __init__(self, val=None, _next=None):
        self.val = val
        self._next = _next

    def __repr__(self):
        return str(self.val)


def f(v=None, prev=None):
    if v is None or v._next is None:
        return v
    n = v._next
    v._next = prev
    return f(n, v)


def f2(head):
    current, prev = head, None
    while current is not None:
        _next = current._next
        current._next = prev
        prev = current
        current = _next
    return prev


def create_linked_list(n=3):
    head = current = Node(0, None)
    for i in range(1, n):
        new = Node(i, None)
        current._next = new
        current = new
    return head


if __name__ == '__main__':
    assert f(create_linked_list()).val, 2
    assert f() is None
    assert f(None) is None

    head = create_linked_list()
    new_head = f(head)
    print(new_head)
    print(new_head._next)