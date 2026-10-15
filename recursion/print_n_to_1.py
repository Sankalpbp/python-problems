def print_n(n):
    if n == 0:
        return
    print(n, end=", ")
    print_n(n - 1)

print_n(10)
