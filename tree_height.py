from datastruct import ChildrenNode as Node


def get_height(n):
    height = 1
    for c in n.children:
        height = max((height, 1 + get_height(c)))

    return height


def print_tree(n, heads=None):
    heads = heads or []
    heads.append(n)
    for c in n.children:
        print_tree(c, heads)

    return heads


if __name__ == '__main__':
    n8 = Node(8)
    n7 = Node(7, [n8])
    n6 = Node(6)
    n3 = Node(3, [n6, n7])

    n4 = Node(4)
    n5 = Node(5)
    n2 = Node(2, [n4, n5])

    n1 = Node(1, [n2, n3])

    assert get_height(n1) == 4
    assert get_height(n3) == 3
    assert get_height(n7) == 2
    assert get_height(n8) == 1

    print(print_tree(n1))
