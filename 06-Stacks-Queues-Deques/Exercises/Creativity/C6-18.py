import stackarray as Stack

def transfer(S, T):
    """Transfer the contents of stack of S to stack T"""

    while not S.is_empty():
        T.push(S.pop())


# Testing
if __name__ == "__main__":
    S = Stack.ArrayStack()
    T = Stack.ArrayStack()
    U = Stack.ArrayStack()

    S.push(12)
    S.push(10)
    S.push(25)
    print('S initial : ',S)
    transfer(S,T)
    print(T)
    transfer(T,U)
    print(U)
    transfer(U,S)
    print('S after : ',S)
