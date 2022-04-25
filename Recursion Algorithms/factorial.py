def factorial(n):
    # assuming that x is a positive number or 0
    if n >= 1:
        return n * factorial(n-1)

    return 1


x = factorial(3)
print(x)
