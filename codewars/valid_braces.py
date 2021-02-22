def validBraces(string):
    if string == '':
        return False

    if len(string) % 2 != 0:
        return False

    parentheses = {"{}", "[]", "()"}
    while len(string) != 0:
        previous_length = len(string)
        for p in parentheses:
            string = string.replace(p, '')
        if len(string) == previous_length:
            return False
    return True


print(validBraces("(){((())}"))
