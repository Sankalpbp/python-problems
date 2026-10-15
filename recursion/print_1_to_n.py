def print_n(n):
    if n == 0:
        return
    print_n(n - 1)
    print(n, end=", ")

print_n(10)
print()
print_n(5)
