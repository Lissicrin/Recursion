import sys

sys.setrecursionlimit(5000)

def recursion(x):
    print(f"Вызов номер {x}")
    if x == 1414:
        return x
    recursion(x+1)
    return None


recursion(1)

def print_list(y):
    print(y.pop(0))
    if len(y) == 0:
        return
    print_list(y)


print_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])