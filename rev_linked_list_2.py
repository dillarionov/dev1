from datastruct import NextNode as Node


def recusrive_reverse(v, prev=None):
    if v is None or v._next is None:
        return v

    next = v._next
    v._next = prev

    return recusrive_reverse(next, v)


def f(v=None, prev=None):
    if v is None or v._next is None:
        v._next = prev
        return v
    n = v._next
    v._next = prev
    return f(n, v)


def recurse(n, last=None):
    if n is None:
        return last
    nxt = n._next
    n._next = last
    return recurse(nxt, n)


def plain_reverse(v):
    current = v
    prev = None

    while current is not None:
        temp = current._next
        current._next = prev
        prev = current
        current = temp

    return prev


if __name__ == '__main__':
    head = Node(0,
                Node(1,
                     Node(2,
                          Node(3))))
    new_head = plain_reverse(head)
    pass
