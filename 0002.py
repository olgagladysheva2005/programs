def summ(chislo):
    if chislo > 0:
        return print(sum([int(i) for i in range(1, chislo + 1)]))
    return print(sum([int(i) for i in range(chislo, 2)]))


summ(int(input()))
