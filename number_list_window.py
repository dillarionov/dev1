from datastruct import Stack


def naive(row, m):
    """O(n * m)"""
    mins = []

    for i in range(0, len(row) - m + 1):
        mins.append(min(row[i:i + m]))

    return mins


def opt(row, m):
    """O(n + m)"""
    pass


if __name__ == '__main__':
    row = [5, 1, 3, 2, 4, 6, 1, 7, 3, 2, 8, ]
    m = 3

    testcase = [1, 1, 2, 2, 1, 1, 1, 2, 2, ]
    assert naive(row, m) == testcase
    assert opt(row, m) == testcase
