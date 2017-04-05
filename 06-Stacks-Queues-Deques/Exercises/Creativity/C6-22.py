import stackarray as Stack

def postfix(expr):
    """Returns the postfix expression of the given infix expr"""

    precedence = ['(',')','^','/','*','+','-']
    postfix_expr = []

    stack = Stack.ArrayStack()

    for char in expr:
        if char in precedence:
            if precedence.index(char) == 0:             # opening paranthesis
                stack.push(char)
            elif precedence.index(char) == 1:           # closing paranthesis
                while not stack.is_empty():
                    res = stack.pop()
                    if res == '(':
                        break
                    postfix_expr.append(res)
            else:                                       # other operators
                if len(stack) > 0 and precedence.index(char) > precedence.index(stack.top()):

                    while len(stack) > 0 and precedence.index(char) > precedence.index(stack.top()):
                        if stack.top() != '(':
                            postfix_expr.append(stack.pop())
                        else:
                            break

                    stack.push(char)
                else:
                    stack.push(char)
        else:
            postfix_expr.append(char)

    while not stack.is_empty():
        postfix_expr.append(stack.pop())

    return ''.join(postfix_expr)

# Testing
if __name__ == "__main__":
    print(postfix('(A+B)*(C-D)/(E*F)'))
    print(postfix('(A/B^C-D)'))
    print(postfix('((5+2)∗(8-3))/4'))