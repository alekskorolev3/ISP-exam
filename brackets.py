def check(str, *args):
    stack = []

    opened = []

    closed = []

    for v in args:
        opened.append(v[0])
        closed.append(v[1])

    for el in str:
        if el in opened:
            stack.append(el)
        elif el in closed:
            if len(stack) == 0:
                raise Exception(")))")

            last = stack.pop(len(stack) - 1)

            index = 0
            for bracket in opened:
                if last == bracket:
                    if not el == closed[index]:
                        raise Exception("Error")
                index += 1

        else:
            raise Exception("Bracket not in args")

    return True

print(check("(({}))", ("(", ")"), ("[", "]")))