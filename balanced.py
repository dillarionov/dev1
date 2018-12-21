from datastruct import Stack


def is_balanced(test_string=''):
    stack = Stack()
    brackets = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    try:
        for char in test_string:
            if char in brackets.keys():
                stack.push(char)
            else:
                assert brackets[stack.pop()] == char
    except IndexError:  # more enclosing brackets than opening
        return False
    except AssertionError:  # not a matching closing bracket
        return False

    return stack.is_empty()


if __name__ == '__main__':

    testcases = (
        ('', True,),
        (']', False,),
        ('{', False,),
        ('()((()(())))()', True,),
        ('()((()((())))))', False,),
        ('[]()[{{{{()([]{{[{{}}]}})}[]{()}}}[]}]{}', True,),
        ('([)]', False,),
    )
    for test_string, result in testcases:
        assert is_balanced(test_string) == result
