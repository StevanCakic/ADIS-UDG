# 1, 2, 3, 4, 5
def suma(array):
    if len(array) == 0:
        return 0
    return array[len(array) - 1] + suma(array[0:len(array) - 1])
    # return array[0] + suma(array[1:])


def factorial(n):
    # return 1 if n == 0 else n * factorial(n - 1)
    if n == 0:
        return 1
    return n * factorial(n - 1)


niz = [1, 2, 3, 4, 5]
print(suma(niz))
print(factorial(4))
