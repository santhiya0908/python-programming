def calculate(expression):
    stack = []
    num = 0
    sign = 1
    result = 0
    for ch in expression:
        if ch.isdigit():
            num = num*10 + int(ch)
        elif ch == '+':
            result += sign * num
            num = 0
            sign = 1
        elif ch == '-':
            result += sign * num
            num = 0
            sign = -1
        elif ch == '*':
            stack.append(result)
            stack.append(sign)
            sign = 1
            result = num
            num = 0
        elif ch == '/':
            stack.append(result)
            stack.append(sign)
            sign = 1
            result = num
            num = 0
        elif ch == ')':
            result += sign * num
            num = 0
            result *= stack.pop()
            result += stack.pop()
    if num:
        result += sign * num
    return result

expression = "1 + 2 * 3 - 4 / 2"
print("The result of the expression '{}' is: {}".format(expression, calculate(expression)))
