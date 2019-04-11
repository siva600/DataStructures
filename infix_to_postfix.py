from stack import Stack


def infix_to_Postfix(infixexpr):
    stack = Stack()
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            topToken = stack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = stack.pop()

        else:
            while (not stack.isempty()) and (prec[stack.peek()] >= prec[token]):
                postfixList.append(stack.pop())
                print(stack.items)
            stack.push(token)

    while not stack.isempty():
        postfixList.append(stack.pop())
        print()
    return " ".join(postfixList)


print(infix_to_Postfix("2 3 * 4 +"))