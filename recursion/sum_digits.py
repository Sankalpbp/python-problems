def sum_digits(n : int) -> int:
    if n == 0:
        return 0
    return (n % 10) + sum_digits(int(n / 10))

print(sum_digits(11111))
print(sum_digits(1234))
