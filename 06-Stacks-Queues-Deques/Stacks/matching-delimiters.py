import stackarray as Stack

def is_matched(expr):
    """Returns True if all the delimiters are matched properly;False otherwise."""
    S = Stack.ArrayStack()
    left = '({['
    right = ')}]'
    for c in expr:
        if c in left:
            S.push(c)
        elif c in right:
            if S.is_empty():
                return False
            if right.index(c) != left.index(S.pop()):
                return False
    return S.is_empty()

# Testing
if __name__ == "__main__":
    print(is_matched('[(5+x)-(6-y)]'))
    print(is_matched('{2*3+(x - 7 + [14-17])}'))
    print(is_matched('(23(12)]'))

