def precedence(op):
    if op in ['+', '-']:
        return 1
    if op in ['*', '/']:
        return 2
    if op == '^':
        return 3
    return 0


def infix_to_postfix(infix):
    stack = []
    postfix = ""

    for ch in infix:

        if ch == ' ':
            continue

        if ch.isalnum():
            postfix += ch

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while len(stack) > 0 and stack[-1] != '(':
                postfix += stack.pop()

            if len(stack) == 0:
                print("ERROR: mismatched brackets")
                return ""

            stack.pop()

        else:
            while len(stack) > 0 and precedence(stack[-1]) >= precedence(ch):
                postfix += stack.pop()

            stack.append(ch)

    while len(stack) > 0:
        if stack[-1] == '(':
            print("ERROR: mismatched brackets")
            return ""
        postfix += stack.pop()

    return postfix


# TEST
expr = "(A + 5) * (B - 3) + C * (D + 2)"
print(infix_to_postfix(expr))