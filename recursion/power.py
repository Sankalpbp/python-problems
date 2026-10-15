def power(x, n):
    if n < 0:
        return 1 / power(x, abs(n))
    if n == 0:
        return 1

    return x * power(x, n - 1)

print(power(5, 2))
print(power(8, 3))
print(power(10, 3))
print(power(10, -3))
