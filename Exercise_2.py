# Define operator precedence
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


def infix_to_postfix(expression):
    """Convert infix expression to postfix"""
    output = []
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isnumeric():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('
        else:  # operator
            while stack and precedence(token) <= precedence(stack[-1]):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return ' '.join(output)


def evaluate_postfix(expression):
    """Evaluate postfix expression"""
    stack = []
    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }

    for token in expression.split():
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            stack.append(operators[token](a, b))
        else:
            stack.append(float(token))

    return stack.pop()


# Example usage
if __name__ == "__main__":
    # Test Case 1 
    expression1 = "( 10 + 2 ) * 6"
    postfix1 = infix_to_postfix(expression1)
    result1 = evaluate_postfix(postfix1)
    print("Infix:", expression1)
    print("Postfix:", postfix1)
    print("Result:", result1)
    print("----")

    # Test Case 2
    expression2 = "3 + 4 * 2"
    postfix2 = infix_to_postfix(expression2)
    result2 = evaluate_postfix(postfix2)
    print("Infix:", expression2)
    print("Postfix:", postfix2)
    print("Result:", result2)
    print("----")

    # Test Case 3
    expression3 = "( 7 + 3 ) / 2"
    postfix3 = infix_to_postfix(expression3)
    result3 = evaluate_postfix(postfix3)
    print("Infix:", expression3)
    print("Postfix:", postfix3)
    print("Result:", result3)