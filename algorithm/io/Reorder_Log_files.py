s = eval(input())  # for input list (or any equation function : using eval())


def reorderLogFiles(logs:list[str]) -> list[str]:
    letters, digits = [], []

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # sort by lambda func, with 2 keys
    letters.sort(key= lambda x: (x.split()[1:], x.split()[0]))

    return letters + digits

print(reorderLogFiles(s))