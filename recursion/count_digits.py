def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(int(n / 10))

print(count_digits(10))
print(count_digits(123))
print(count_digits(0))
