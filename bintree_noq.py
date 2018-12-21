class Node:

    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def print_as_tree(self):
        if self.left is not None:
            print('(', end='')
            self.left.print_as_tree()
            print(') ', end='')
        print(self.data, end='')
        if self.right is not None:
            print(' (', end='')
            self.right.print_as_tree()
            print(')', end='')

    def print_as_list(self):
        t = self
        while t is not None:
            print(t.data, end=' ')
            t = t.right

    def __repr__(self):
        return str(self.data)


def tolist(l):
    # IMPLEMENT THIS
    pass


if __name__ == '__main__':
    l1 = Node(1, None, None)
    l2 = Node(3, None, None)
    l3 = Node(2, l1, l2)
    l4 = Node(5, None, None)
    l5 = Node(7, None, None)
    l6 = Node(6, l4, l5)
    l7 = Node(4, l3, l6)

    l7.print_as_tree()
    print()

    # l, r = tolist(l7)

    l7.print_as_list()
