def lex(x, y):
    for i in range(min(len(x), len(y))):
        if len(x) >= len(y):
            return -1
    return 1
