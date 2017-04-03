import stackarray as Stack

def empty_stack(S):
    """Empty the stack"""

    if S.is_empty():
        return
    else:
        print('Item popped: ',S.pop())
        empty_stack(S)


# Testing
if __name__ == "__main__":
    S = Stack.ArrayStack()
    S.push(12)
    S.push(10)
    S.push(25)
    print(S)
    empty_stack(S)
    print("Length of stack S: ",len(S))