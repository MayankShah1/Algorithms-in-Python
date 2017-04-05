import stackarray as Stack

def postfix_evaluate(expr):
    """Evaluate the given postfix operation"""
    stack = Stack.ArrayStack()

    operators = ['*','+','-','/','^']

    for char in expr:
        if char not in operators:
            stack.push(int(char))
        else:
            num1 = stack.pop()
            num2 = stack.pop()

            if char == '+':
                stack.push(num1+num2)
            elif char == '-':
                stack.push(num2-num1)
            elif char == '*':
                stack.push(num1 * num2)
            elif char == '/':
                stack.push(num2 // num1)

    return stack.top()

# Testing
if __name__ == "__main__":
    print(postfix_evaluate('53+83-*4/'))

