class Node():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        # FIXME: expensive insert
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def IntGenerator(to=7):
    for i in range(to):
        yield i


def create_binary_tree(depth=3):
    """Creates binary with with specified sizes.

    :param depth: tree depth
    :return: tree root Node
    """
    # The only node is root
    max_nodes, nodes = 2 ** depth - 1, 1
    queue = Queue()
    val = IntGenerator()
    root = Node(val=next(val))

    queue.enqueue(root)
    while nodes + 2 <= max_nodes:
        current = queue.dequeue()

        # Create child nodes until total num is le max_nodes
        # for specified length in binary tree
        if nodes + 2 <= max_nodes:  # tree will have +2 nodes after creating children
            current.left = Node(val=next(val))
            current.right = Node(val=next(val))
            queue.enqueue(current.left)
            queue.enqueue(current.right)
            nodes += 2

    return root


def traverse_tree_width(root):
    """Visits and returns all nodes' values using width traversal.

    :param root: tree root node
    :return: visited nodes' values
    """
    values = []
    queue = Queue()

    queue.enqueue(root)
    while queue.isEmpty() is False:
        node = queue.dequeue()
        values.append(node.val)

        # if current node has children, add it to queue
        if node.left and node.right:
            queue.enqueue(node.left)
            queue.enqueue(node.right)

    return values


if __name__ == '__main__':
    root = create_binary_tree()

    assert traverse_tree_width(root), [0, 1, 2, 3, 4, 5, 6]
