def fib(n):
    # assuming n is a positive integer
    if n >= 3:
        return fib(n-1) + fib(n-2)

    return 1


fibonacci_list = [0]

for x in range(1, 7):
    fibonacci_list.append(fib(x))


print(fibonacci_list)
